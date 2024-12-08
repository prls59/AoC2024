import os

DATAFILE = "input.txt"

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

STEP = [(0,-1),(1,0),(0,1),(-1,0)]

CUR_LOCATION = 0
FACING = 1
START_LOCATION = 2

CLEAR = '.'
OBSTACLE = '#'
GUARD_START = '^'
CRUMB = '*'

def guard_patrol(lab_map, guard):
    in_lab = True
    while in_lab:
        new_x = guard[CUR_LOCATION][0]+STEP[guard[FACING]][0]
        new_y = guard[CUR_LOCATION][1]+STEP[guard[FACING]][1]
        if new_x < 0 or new_x >= lab_width or new_y < 0 or new_y >= lab_length:
            in_lab = False
        elif lab_map[new_y][new_x] == OBSTACLE:
            guard[FACING] = (guard[FACING] + 1) % 4
        else:
            # A clear space is ahead - add a temporary obstacle
            # and look for potential loop, provided guard hasn't
            # passed through the space already.
            if lab_map[new_y][new_x] != CRUMB:
                lab_map[new_y][new_x] = OBSTACLE
                if loopy(lab_map, guard):
                    poss_obs = (new_x, new_y)
                    possible_obstructions.add(poss_obs)
            guard[CUR_LOCATION] = [new_x, new_y]
            lab_map[new_y][new_x] = CRUMB

def loopy(lab_map, guard):

    # directional crumbs
    NO_CRUMB = 0b00000000
    CRUMB_N = 0b00000001
    CRUMB_E = 0b00000010
    CRUMB_S = 0b00000100
    CRUMB_W = 0b00001000

    CRUMB_FACE = [CRUMB_N, CRUMB_E, CRUMB_S, CRUMB_W]

    detour = {}
    found_loop = False
    in_lab = True
    look_x = guard[CUR_LOCATION][0]
    look_y = guard[CUR_LOCATION][1]
    looking = guard[FACING]
    detour[(look_x, look_y)] = CRUMB_FACE[looking]

    while in_lab and not found_loop:

        look_x += STEP[looking][0]
        look_y += STEP[looking][1]

        if look_x < 0 or look_x >= lab_width or look_y < 0 or look_y >= lab_length:
            in_lab = False
            break
        elif lab_map[look_y][look_x] == OBSTACLE:
            # step back & turn right
            look_x -= STEP[looking][0]
            look_y -= STEP[looking][1]
            looking = (looking + 1) % 4

        cur_crumb = detour.get((look_x, look_y), NO_CRUMB)
        if cur_crumb & CRUMB_FACE[looking] == CRUMB_FACE[looking]:
            found_loop = True
        else:
            cur_crumb |= CRUMB_FACE[looking]
            detour[(look_x, look_y)] = cur_crumb

    return found_loop

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    rows = input.read()[0:-1].split("\n")

lab_width = len(rows[0])
lab_length = len(rows)

guard = [[], NORTH, []]
found_guard = False

lab_map = []
for y in range(lab_length):
    lab_map.append([rows[y][x] for x in range(lab_width)])
    if not found_guard:
        try:
            x = rows[y].index(GUARD_START)
            guard[START_LOCATION] = [x, y]
            guard[CUR_LOCATION] = [x, y]
            lab_map[y][x] = CRUMB
            found_guard = True
        except ValueError:
            pass

possible_obstructions = set()
guard_patrol(lab_map, guard)

print('Result = ', len(possible_obstructions))