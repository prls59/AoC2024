import os, re
from collections import defaultdict

datafile = "input.txt"

unique_locations = set()
antennae = defaultdict(list)
city_limits = []

def find_antinodes(ant1, ant2, unique_locations, city_limits):
    dx = ant1[0] - ant2[0]
    dy = ant1[1] - ant2[1]
    new_x = ant1[0] + dx
    new_y = ant1[1] + dy
    if new_x >=0 and new_x < city_limits[0] and new_y >=0 and new_y < city_limits[1]:
        unique_locations.add((new_x, new_y))
    new_x = ant2[0] - dx
    new_y = ant2[1] - dy
    if new_x >=0 and new_x < city_limits[0] and new_y >=0 and new_y < city_limits[1]:
        unique_locations.add((new_x, new_y))

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    y = 0
    width = 0
    for line in input:
        width = len(line) - 1
        antenna_matches = re.finditer('[a-zA-Z0-9]', line[:-1])
        for antenna_match in antenna_matches:
            antennae[antenna_match.group(0)].append([antenna_match.start(),y])
        y += 1
    city_limits = [width, y]

for antenna_freq in iter(antennae):
    linked_antennae = antennae.get(antenna_freq)
    linked_count = len(linked_antennae)
    if linked_count > 1:
        for a in range(linked_count - 1):
            for b in range(a + 1, linked_count):
                  find_antinodes(linked_antennae[a], linked_antennae[b], unique_locations, city_limits)

print('Result = ', len(unique_locations))