import os, queue

DATAFILE = "input.txt"

# Directions
STEP = [(0,-1),(1,0),(0,1),(-1,0)]
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Map legend
WALL = '#'
START = 'S'
END = 'E'
SPACE = '.'

# Costs
STEP_COST = 1
TURN_COST = 1000

def next_poi(maze, loc_head, end_loc):
    ((x,y), head) = loc_head
    left = (head + 3) % 4
    right = (head + 1) % 4
    
    while True:
        x = x + STEP[head][0]
        y = y + STEP[head][1]
        # Stop if blocked &/or junction
        if (maze[y + STEP[head][1]][x + STEP[head][0]] == WALL
            or maze[y + STEP[left][1]][x + STEP[left][0]] != WALL
            or maze[y + STEP[right][1]][x + STEP[right][0]] != WALL):
            break

    return ((x, y), head)

def available_locs(maze, curr_loc_head, end_loc):
    steps = []
    (curr_loc, curr_head) = curr_loc_head

    head = (curr_head + 3) % 4

    dead_end = True
    for n in range(3):
        if maze[curr_loc[1] + STEP[head][1]][curr_loc[0] + STEP[head][0]] != WALL:
            dead_end = False
            steps.append((next_poi(maze, (curr_loc, head), end_loc)))
        head = (head + 1) % 4

    if dead_end:
        head = (curr_head + 2) % 4
        steps.append((next_poi(maze, (curr_loc, head), end_loc)))

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
            break

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
                priority = new_cost
                frontier.put((priority, next_loc_head))
                from_dict[next_loc_head] = curr_loc_head

    return from_dict, cost_dict

maze = []
with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    data = input.read()
rows = data[:-1].split("\n")
for row in rows:
    maze.append([x for x in row])

start_loc_head = ((1, len(maze) - 2), EAST)
end_loc = (len(maze[0]) - 2, 1)

from_dict, cost_dict = dijkstra(maze, start_loc_head, end_loc)

shortest = -1
end = ()
for loc_head in cost_dict.keys():
    (loc, _) = loc_head
    if loc == end_loc:
        if shortest == -1 or cost_dict[loc_head] < shortest:
            shortest = cost_dict[loc_head]
            end = loc_head

print('Result = ', shortest)