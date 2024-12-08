import os

DATAFILE = "input.txt"

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

STEP = [(0,-1),(1,0),(0,1),(-1,0)]

LOCATION = 0
FACING = 1
IN_LAB = 2

OBSTACLE = '#'
START_POS = '^'
VISITED = 'X'

def patrol(lab_map, guard):
    clear_path = True
    while clear_path:
        new_x = guard[LOCATION][0]+STEP[guard[FACING]][0]
        new_y = guard[LOCATION][1]+STEP[guard[FACING]][1]
        if new_x < 0 or new_x >= lab_width or new_y < 0 or new_y >= lab_length:
            clear_path = False
            guard[IN_LAB] = False
        elif lab_map[new_y][new_x] == OBSTACLE:
            clear_path = False
            guard[FACING] = (guard[FACING] + 1) % 4
        else:
            lab_map[new_y][new_x] = VISITED
            guard[LOCATION][0] = new_x
            guard[LOCATION][1] = new_y

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    rows = input.read()[0:-1].split("\n")

lab_width = len(rows[0])
lab_length = len(rows)

guard = [[-1,-1], NORTH, False]

lab_map = []
for y in range(lab_length):
    lab_map.append([rows[y][x] for x in range(lab_width)])
    if not guard[IN_LAB]:
        try:
            x = rows[y].index('^')
            guard[LOCATION] = [x, y]
            guard[IN_LAB] = True
            lab_map[y][x] = VISITED
        except ValueError:
            pass

while guard[IN_LAB]:
    patrol(lab_map, guard)

visited_positions = 0
for row in lab_map:
    for position in row:
        if position == VISITED:
            visited_positions += 1

print('Result = ', visited_positions)