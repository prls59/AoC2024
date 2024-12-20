import os
from collections import defaultdict

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

SAVING = 100
CHEAT_COST = 2

track_map = []
track = defaultdict(list)
track_length = 0

def in_bounds(loc):
    return (0 <= loc[0] < dimensions[0] and 0 <= loc[1] < dimensions[1])

def track_walk(track_map, start, end, heading, track):
    loc = start
    ps = 0
    while loc != end:
        # Look around for potential cheats...
        cheats = []
        for n in range(4):
            check = (loc[0] + STEP[n][0] * 2, loc[1] + STEP[n][1]* 2)
            if (in_bounds(check)
                and track_map[check[1]][check[0]] in [SPACE, END]
                and not check in track):
                cheats.append(check)
        # record track location, time taken & any cheats
        track[tuple(loc)] = [ps, cheats]
        # step forward
        loc = [loc[n] + STEP[heading][n] for n in range(2)]
        ps += 1
        if tuple(loc) == end:
            track[tuple(loc)] = [ps, []]
            break
        # Otherwise, get next heading (left, ahead or right...)
        left = (heading + 3) % 4
        for look in range(left, left + 3):
            heading = look % 4
            if track_map[loc[1] + STEP[heading][1]][loc[0] + STEP[heading][0]] in [SPACE, END]:
                break

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    for y, row in enumerate(input.read()[0:-1].split("\n")):
        track_map.append([x for x in row])
        if row.find(START) >= 0:
            start = (row.find(START), y)
        if row.find(END) >= 0:
            end = (row.find(END), y)
    dimensions = (len(track_map[0]), y+1)

# Get initial heading
for heading in range(4):
    loc = [start[n] + STEP[heading][n] for n in range(2)]
    if track_map[loc[1]][loc[0]] == SPACE:
        break

# survey track
track_walk(track_map, start, end, heading, track)
track_length = len(track)

shortcut_count = 0
for (ps, cheats) in track.values():
    if ps > track_length - SAVING - 2:
        break
    for shortcut in cheats:
        if track[shortcut][0] - (ps + CHEAT_COST) >= SAVING:
            shortcut_count += 1

print('Result = ', shortcut_count)