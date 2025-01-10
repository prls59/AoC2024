import os, queue

EXAMPLE = False

if EXAMPLE:
    DATAFILE = "example.txt"
    X_LIMIT = 7
    Y_LIMIT = 7
else:
    DATAFILE = "input.txt"
    X_LIMIT = 71
    Y_LIMIT = 71

STEPS = [(0,-1), (0,1), (-1,0), (1,0)]

bytes = []

def in_bounds(loc):
    return (0 <= loc[0] < X_LIMIT and 0 <= loc[1] < Y_LIMIT)

def available_locs(curr_loc, ns):
    steps = []

    for s in range(len(STEPS)):
        new_loc = (curr_loc[0] + STEPS[s][0], curr_loc[1] + STEPS[s][1])
        if in_bounds(new_loc) and new_loc not in bytes[:ns]:
            steps.append(new_loc)
    return steps

def path(start_loc, end_loc, ns):
    frontier = queue.PriorityQueue()
    frontier.put((0, start_loc))
    from_dict = {}
    cost_dict = {}
    from_dict[start_loc] = None
    cost_dict[start_loc] = 0
    
    path_found = False
    while not frontier.empty():
        (_, curr_loc) = frontier.get()
        
        if curr_loc == end_loc:
            path_found = True
            break
        else:
            next_locs = available_locs(curr_loc, ns)
            for next_loc in next_locs:
                new_cost = cost_dict[curr_loc] + 1

                if next_loc not in cost_dict or new_cost < cost_dict[next_loc]:
                    cost_dict[next_loc] = new_cost
                    priority = new_cost
                    frontier.put((priority, next_loc))
                    from_dict[next_loc] = curr_loc

    return path_found

def judo_chop(bytes, start_loc, end_loc):
    low = 0
    high = len(bytes)
    ns = 0

    while low <= high:
        ns = (high + low) // 2
        if path(start_loc, end_loc, ns):
            low = ns + 1
        else:
            if path(start_loc, end_loc, ns - 1):
                return ns - 1
            high = ns - 1
    return ns

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    rows = input.read()[0:-1].split("\n")

for row in rows:
    bytes.append(tuple(map(int, row.split(','))))

start_loc = (0,0)
end_loc = (X_LIMIT - 1, Y_LIMIT - 1)

print('Result = ', bytes[judo_chop(bytes, start_loc, end_loc)])