import os

datafile = "input.txt"

loc_lists = [[],[]]

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for line in input:
        locs = line[0:-1].split()
        loc_lists[0].append(int(locs[0]))
        loc_lists[1].append(int(locs[1]))

l0_locations = set(loc_lists[0])

factors = []
for loc in l0_locations:
    l1_count = loc_lists[1].count(loc)
    if l1_count > 0:
        factors.append([loc, loc_lists[0].count(loc), l1_count])

result = sum(fact[0] * fact[1] * fact[2] for fact in factors)

print('Result = ', result)