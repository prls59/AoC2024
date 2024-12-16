import os

DATAFILE = "input.txt"

DIRECTION = ['^', '>', 'v', '<']
STEP = [(0,-1),(1,0),(0,1),(-1,0)]
WALL = '#'
BOX = 'O'
ROBOT = '@'
SPACE = '.'

location = [0,0]
warehouse = []
program = ''

def drive(location, step):
    new_loc = [location[0] + step[0], location[1] + step[1]]
    encounter = warehouse[new_loc[1]][new_loc[0]]
    if encounter == BOX:
        push_boxes(location, step)
    elif encounter != WALL:
        warehouse[location[1]][location[0]] = SPACE # not really necessary...
        location[:] = new_loc
        warehouse[location[1]][location[0]] = ROBOT # not really necessary...

def push_boxes(location, step):
    box_count = 0
    space_found = False
    new_loc = location
    while not space_found:
        new_loc = [new_loc[0] + step[0], new_loc[1] + step[1]]
        encounter = warehouse[new_loc[1]][new_loc[0]]
        if encounter == WALL:
            break
        elif encounter == BOX:
            box_count += 1
        else:
            space_found = True
    if space_found:
        warehouse[location[1]][location[0]] = SPACE
        warehouse[location[1] + step[1]][location[0] + step[0]] = ROBOT
        for n in range(box_count):
            warehouse[location[1] + (n+2) * step[1]][location[0] + (n+2) * step[0]] = BOX
        location[:] = [location[0] + step[0], location[1] + step[1]]

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
            warehouse.append([x for x in line])
            try:
                x = line.index(ROBOT)
                location = [x, y]
            except ValueError:
                pass
            y += 1
        else:
            program += line

dimensions = (len(warehouse[0]), y)
prog_length = len(program)

for p in range(prog_length):
    drive(location, STEP[DIRECTION.index(program[p])])

gps_sum = 0
for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        if warehouse[y][x] == BOX:
            gps_sum += x + 100 * y

print('Result = ', gps_sum)