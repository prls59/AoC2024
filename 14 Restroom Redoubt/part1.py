import os, re

DATAFILE = "input.txt"

# DIMENSIONS = (11, 7)      # example
DIMENSIONS = (101, 103)   # input

INTERVAL = 100

location = [0,0]
midpoint = [DIMENSIONS[0]//2, DIMENSIONS[1]//2]
quadrants = [0, 0, 0, 0]

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    for line in input:
        values = [int(x) for x in re.findall(r'(-?\d+)', line)]
        location[0] = (values[0] + values[2] * INTERVAL) % DIMENSIONS[0]
        location[1] = (values[1] + values[3] * INTERVAL) % DIMENSIONS[1]
        if location[0] < midpoint[0]:
            if location[1] < midpoint[1]:
                quadrants[0] += 1
            elif location[1] > midpoint[1]:
                quadrants[1] += 1
        elif location[0] > midpoint[0]:
            if location[1] < midpoint[1]:
                quadrants[2] += 1
            elif location[1] > midpoint[1]:
                quadrants[3] += 1

safety_factor = 1
for robots in quadrants:
    safety_factor *= robots

print('Result = ', safety_factor)