import os

datafile = "input.txt"

loc_lists = [[],[]]

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        locs = line[0:-1].split()
        loc_lists[0].append(int(locs[0]))
        loc_lists[1].append(int(locs[1]))

loc_lists[0].sort()
loc_lists[1].sort()

tot_dist = sum(abs(loc_lists[0][n] - loc_lists[1][n]) for n in range(len(loc_lists[0])))

print('Result = ', tot_dist)