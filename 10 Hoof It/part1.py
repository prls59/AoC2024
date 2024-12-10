import os

DATAFILE = "input.txt"

hiking_map = []

def find_trails(hiking_map, dimensions, location, peaks):
    steps = [(-1,0),(0,-1),(1,0),(0,1)]
    next_height = hiking_map[location[1]][location[0]] + 1
    for step in steps:
        new_loc = [location[0] + step[0],location[1] + step[1]]
        if (new_loc[0] >= 0 and new_loc[0] < dimensions[0]
            and new_loc[1] >= 0 and new_loc[1] < dimensions[1]):
            if hiking_map[new_loc[1]][new_loc[0]] == next_height:
                if next_height == 9:
                    peaks[:] = peaks[:] + [new_loc]
                else:
                    find_trails(hiking_map, dimensions, new_loc, peaks)

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    for y, row in enumerate(input.read()[0:-1].split("\n")):
        hiking_map.append([int(x) for x in row])
    dimensions = (len(hiking_map[0]), y+1)

trail_scores = 0

for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        if hiking_map[y][x] == 0:
            peaks = []
            find_trails(hiking_map, dimensions, (x, y), peaks)
            unique_peaks = set()
            for peak in peaks:
                unique_peaks.add(tuple(peak))
            trail_scores += len(unique_peaks)

print('Result = ', trail_scores)