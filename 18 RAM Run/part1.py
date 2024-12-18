import os, queue

DATAFILE = "input.txt"

EXAMPLE = False

if EXAMPLE:
    X_LIMIT = 7
    Y_LIMIT = 7
    NS = 12
else:
    X_LIMIT = 71
    Y_LIMIT = 71
    NS = 1024

STEPS = [(0,-1), (0,1), (-1,0), (1,0)]

CLEAR = '.'
BYTE = '#'

bytes = []
mem_space = []

def in_bounds(loc):
    return (0 <= loc[0] < X_LIMIT and 0 <= loc[1] < Y_LIMIT)

def available_locs(mem_space, curr_loc):
    steps = []

    for s in range(len(STEPS)):
        new_loc = (curr_loc[0] + STEPS[s][0], curr_loc[1] + STEPS[s][1])
        if in_bounds(new_loc) and mem_space[new_loc[1]][new_loc[0]] != BYTE:
            steps.append(new_loc)
    return steps

def dijkstra(mem_space, start_loc, end_loc):
    frontier = queue.PriorityQueue()
    frontier.put((0, start_loc))
    from_dict = {}
    cost_dict = {}
    from_dict[start_loc] = None
    cost_dict[start_loc] = 0
    
    while not frontier.empty():
        (_, curr_loc) = frontier.get()
        
        if curr_loc == end_loc:
            break

        next_locs = available_locs(mem_space, curr_loc)
        for next_loc in next_locs:
            new_cost = cost_dict[curr_loc] + 1

            if next_loc not in cost_dict or new_cost < cost_dict[next_loc]:
                cost_dict[next_loc] = new_cost
                priority = new_cost
                frontier.put((priority, next_loc))
                from_dict[next_loc] = curr_loc

    return from_dict, cost_dict

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    rows = input.read()[0:-1].split("\n")

for row in rows:
    bytes.append([int(x) for x in row.split(',')])

for y in range(Y_LIMIT):
    mem_space.append(['.' for x in range(X_LIMIT)])

for n in range(NS):
    mem_space[bytes[n][1]][bytes[n][0]] = BYTE

start_loc = (0,0)
end_loc = (X_LIMIT - 1, Y_LIMIT - 1)

from_dict, cost_dict = dijkstra(mem_space, start_loc, end_loc)

shortest = -1
end = ()
for loc in cost_dict.keys():
    if loc == end_loc:
        if shortest == -1 or cost_dict[loc] < shortest:
            shortest = cost_dict[loc]
            end = loc

print('Result = ', shortest)