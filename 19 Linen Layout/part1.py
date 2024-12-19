import os

DATAFILE = "input.txt"

def possible(design, towels, limits):
    len_design = len(design)
    for n in range(min(len_design, limits[1]), limits[0] - 1, -1):
        if design[0:n] in towels:
            if n == len_design:
                return True
            else:
                if possible(design[n:], towels, limits):
                    return True
    return False

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    towels = input.readline()[0:-1].split(', ')
    limits = [-1, 0]
    for towel in towels:
        num_stripes = len(towel)
        if num_stripes < limits[0] or limits[0] == -1:
            limits[0] = num_stripes
        elif num_stripes > limits[1]:
            limits[1] = num_stripes
    input.readline()
    design = input.readline()[0:-1]
    poss_count = 0
    while design != '':
        if possible(design, towels, limits):
            poss_count += 1
        design = input.readline()[0:-1]
        
print('Result = ', poss_count)