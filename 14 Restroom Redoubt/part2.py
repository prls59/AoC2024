import os, re

DATAFILE = "input.txt"

# DIMENSIONS = (11, 7)      # example
DIMENSIONS = (101, 103)   # input
MAX_TIME = 1000000000
POSITION = 0
VELOCITY = 1
X = 0
Y = 1

# Search constraints
START_SEQUENCE = 5
MIN_INCREASING_ROWS = 10
MIN_INCREMENT = 2

robots = []

def tannenbaum():
    potential_tree = False
    robots.sort(key=lambda robot: robot[POSITION][Y] * 1000 + robot[POSITION][X])
    seq = 1
    seq_rows = 0
    min_seq = START_SEQUENCE
    seq_found = False
    for n in range(1, len(robots)):
        if robots[n][POSITION][Y] == robots[n-1][POSITION][Y]:
            if abs(robots[n][POSITION][X] - robots[n-1][POSITION][X]) == 1:
                seq += 1
                if seq >= min_seq:
                    seq_rows += 1
                    seq_found = True
                    if seq_rows > MIN_INCREASING_ROWS:
                        potential_tree = True
                        break
                    else:
                        min_seq += MIN_INCREMENT
                        for n in range(n+1, len(robots)):
                            if robots[n][POSITION][Y] != robots[n-1][POSITION][Y]:
                                break
            else:
                seq = 1
        else:
            if not seq_found:
                seq = 1
                seq_rows = 0
                min_seq = START_SEQUENCE
            seq_found = False
    return potential_tree

            

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    for line in input:
        values = [int(x) for x in re.findall(r'(-?\d+)', line)]
        robots.append([[values[0], values[1]], (values[2], values[3])])

for timer in range(1, MAX_TIME):
    for robot in robots:
        robot[POSITION][X] = (robot[POSITION][X] + robot[VELOCITY][X]) % DIMENSIONS[X]
        robot[POSITION][Y] = (robot[POSITION][Y] + robot[VELOCITY][Y]) % DIMENSIONS[Y]
    if tannenbaum():
        christmas_tree = True
        break

if christmas_tree:
    print('Result = ', timer)
else:
    print('Reached max: ', timer)