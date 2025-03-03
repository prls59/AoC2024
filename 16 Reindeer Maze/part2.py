import os, queue

DATAFILE = "input.txt"

# Directions (N, E, S, W)
STEP = [(0,-1),(1,0),(0,1),(-1,0)]

# Map legend
WALL = '#'

# Costs
STEP_COST = 1
TURN_COST = 1000

def available_locs(maze, curr_loc_head, end_loc):
    steps = []
    (curr_loc, curr_head) = curr_loc_head

    head = (curr_head + 3) % 4

    for n in range(3):
        next_loc = (curr_loc[0] + STEP[head][0], curr_loc[1] + STEP[head][1])
        if maze[next_loc[1]][next_loc[0]] != WALL:
            steps.append((next_loc, head))
        head = (head + 1) % 4

    return steps

def dijkstra(maze, start_loc_head, end_loc):
    frontier = queue.PriorityQueue()
    frontier.put((0, start_loc_head))
    from_dict = {}
    cost_dict = {}
    from_dict[start_loc_head] = None
    cost_dict[start_loc_head] = 0
    
    while not frontier.empty():
        (_, curr_loc_head) = frontier.get()
        
        (curr_loc, curr_head) = curr_loc_head
        if curr_loc == end_loc:
            continue

        next_loc_heads = available_locs(maze, curr_loc_head, end_loc)
        for next_loc_head in next_loc_heads:
            (next_loc, next_head) = next_loc_head
            new_cost = (cost_dict[curr_loc_head]
                        + abs(next_loc[0] - curr_loc[0]) * STEP_COST
                        + abs(next_loc[1] - curr_loc[1]) * STEP_COST)
            if next_head != curr_head:
                new_cost += TURN_COST
            if next_head == (curr_head + 2) % 4:
                new_cost += TURN_COST   # u-turn

            if next_loc_head not in cost_dict or new_cost < cost_dict[next_loc_head]:
                cost_dict[next_loc_head] = new_cost
                from_dict[next_loc_head] = curr_loc_head
                frontier.put((new_cost, next_loc_head))
            elif new_cost == cost_dict[next_loc_head]:
                from_dict[next_loc_head] = curr_loc_head

    return from_dict, cost_dict

maze = []
with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    data = input.read()
rows = data[:-1].split("\n")
for row in rows:
    maze.append([x for x in row])

start_loc = (1, len(maze) - 2)
start_loc_head = (start_loc, 1)
end_loc = (len(maze[0]) - 2, 1)

from_dict, cost_dict = dijkstra(maze, start_loc_head, end_loc)

min_cost = -1
for loc_head in cost_dict.keys():
    (loc, _) = loc_head
    if loc == end_loc:
        if min_cost == -1 or cost_dict[loc_head] < min_cost:
            min_cost = cost_dict[loc_head]

best_spots = set()
best_spots.add(start_loc)
best_spots.add(end_loc)

backwards = queue.Queue()
for loc_head in cost_dict.keys():
    (loc, _) = loc_head
    if loc == end_loc and cost_dict[loc_head] == min_cost:
        backwards.put((loc_head, min_cost))
    
while not backwards.empty():
    (dest_loc_head, dest_cost) = backwards.get()
    (dest_loc, dest_head) = dest_loc_head

    prev_loc = (dest_loc[0] - STEP[dest_head][0], dest_loc[1] - STEP[dest_head][1])
    if prev_loc == start_loc:
        continue

    on_best_path = False
    prev_loc_head = (prev_loc, dest_head)
    if prev_loc_head in cost_dict and dest_cost == cost_dict[prev_loc_head] + STEP_COST:
        backwards.put((prev_loc_head, cost_dict[prev_loc_head]))
        on_best_path = True

    prev_loc_head = (prev_loc, (dest_head + 1) % 4)
    if prev_loc_head in cost_dict and dest_cost == cost_dict[prev_loc_head] + TURN_COST + STEP_COST:
        backwards.put((prev_loc_head, cost_dict[prev_loc_head]))
        on_best_path = True

    prev_loc_head = (prev_loc, (dest_head + 3) % 4)
    if prev_loc_head in cost_dict and dest_cost == cost_dict[prev_loc_head] + TURN_COST + STEP_COST:
        backwards.put((prev_loc_head, cost_dict[prev_loc_head]))
        on_best_path = True

    if on_best_path:
        loc = prev_loc
        while loc != dest_loc:
            best_spots.add(loc)
            loc = (loc[0] + STEP[dest_head][0], loc[1] + STEP[dest_head][1])

print('Result = ', len(best_spots))