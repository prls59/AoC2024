import os

DATAFILE = "input.txt"

# Directions
DIRECTION = ['^', '>', 'v', '<']
STEP = [(0,-1),(1,0),(0,1),(-1,0)]
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Map legend
WALL = '#'
BOX_L = '['
BOX_R = ']'
BOX = 'O'
ROBOT = '@'
SPACE = '.'
DOUBLE = {
            WALL: [WALL, WALL],
            BOX: [BOX_L, BOX_R],
            ROBOT: [ROBOT, SPACE],
            SPACE: [SPACE, SPACE]
        }

location = [0,0]
warehouse = []
program = ''
instruction = ''

def move(location, direction):
    new_loc = [location[0] + STEP[direction][0], location[1] + STEP[direction][1]]
    encounter = warehouse[new_loc[1]][new_loc[0]]
    clear_ahead = False
    if encounter in DOUBLE[BOX]:
        if pushable(new_loc, direction):
            clear_ahead = push(new_loc, direction)
    else:
        clear_ahead = (encounter != WALL)
    if clear_ahead:
        warehouse[location[1]][location[0]] = SPACE
        location[:] = new_loc
        warehouse[location[1]][location[0]] = ROBOT

def pushable(box_loc, direction):
    return push(box_loc, direction, True)

def push(box_loc, direction, just_checking = False):
    moveable = False
    if direction in [EAST, WEST]:
        # horizontal push...
        next_loc = [box_loc[n] + 2 * STEP[direction][n] for n in range(2)]
        encounter = warehouse[next_loc[1]][next_loc[0]]
        if encounter == SPACE:
            moveable = True
        elif encounter in DOUBLE[BOX]:
            moveable = push(next_loc, direction, just_checking)

        if moveable and not just_checking:
            warehouse[box_loc[1]][box_loc[0]] = SPACE
            if direction == EAST:
                warehouse[box_loc[1]][box_loc[0] + 1] = BOX_L
                warehouse[box_loc[1]][box_loc[0] + 2] = BOX_R
            else:
                warehouse[box_loc[1]][box_loc[0] - 1] = BOX_R
                warehouse[box_loc[1]][box_loc[0] - 2] = BOX_L
   
    else:
        # vertical push...
        box_side = warehouse[box_loc[1]][box_loc[0]]
        next_loc = [box_loc[n] + STEP[direction][n] for n in range(2)]
        if box_side == BOX_R:
            next_loc[0] -= 1
        next_l = warehouse[next_loc[1]][next_loc[0]]
        next_r = warehouse[next_loc[1]][next_loc[0] + 1]

        if next_l == SPACE:
            if next_r == SPACE:
                moveable = True
            elif next_r == BOX_L:
                moveable = push([next_loc[0]+1,next_loc[1]], direction, just_checking)
        else:
            if next_l == BOX_L:
                moveable = push(next_loc, direction, just_checking)
            elif next_l == BOX_R:
                if next_r == SPACE:
                    moveable = push(next_loc, direction, just_checking)
                elif next_r == BOX_L:
                    moveable = (push(next_loc, direction, just_checking) and
                                push([next_loc[0]+1,next_loc[1]], direction, just_checking))

        if moveable and not just_checking:
            warehouse[box_loc[1]][box_loc[0]] = SPACE
            if box_side == BOX_L:
                warehouse[box_loc[1]][box_loc[0] + 1] = SPACE
                warehouse[box_loc[1] + STEP[direction][1]][box_loc[0]] = BOX_L
                warehouse[box_loc[1] + STEP[direction][1]][box_loc[0] + 1] = BOX_R
            else:
                warehouse[box_loc[1]][box_loc[0] - 1] = SPACE
                warehouse[box_loc[1] + STEP[direction][1]][box_loc[0]] = BOX_R
                warehouse[box_loc[1] + STEP[direction][1]][box_loc[0] - 1] = BOX_L
    return moveable

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    building_map = True
    y = 0
    for line in input:
        line = line[:-1]
        if line == '':
            if building_map:
                building_map = False
            else:
                break
        elif building_map:
            row = []
            for x in line:
                row.extend(DOUBLE[x])
            warehouse.append(row)
            try:
                x = line.index(ROBOT)
                location = [2 * x, y]
            except ValueError:
                pass
            y += 1
        else:
            program += line

dimensions = (len(warehouse[0]), y)
prog_length = len(program)

for p in range(prog_length):
    instruction = program[p]
    move(location, DIRECTION.index(instruction))

gps_sum = 0
for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        if warehouse[y][x] == BOX_L:
            gps_sum += x + 100 * y

print('Result = ', gps_sum)