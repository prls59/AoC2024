import os

DATAFILE = "input.txt"

STEPS = [(-1,0),(0,-1),(1,0),(0,1)]

garden = []
prices = []

def measure_plot(x, y):
    plant = garden[y][x]
    area = 1
    perimeter = get_perimeter(x, y, plant)
    garden[y][x] = plant.lower()
    for step in STEPS:
        new_x = x + step[0]
        new_y = y+ step[1]
        if (new_x >= 0 and new_x < dimensions[0]
            and new_y >= 0 and new_y < dimensions[1]):
            if garden[new_y][new_x] == plant:
                    [sub_area, sub_permieter] = measure_plot(new_x, new_y)
                    area += sub_area
                    perimeter += sub_permieter
    return [area, perimeter]

def get_perimeter(x, y, plant):
    perimeter = 0
    for step in STEPS:
        new_x = x + step[0]
        new_y = y+ step[1]
        if (new_x >= 0 and new_x < dimensions[0]
            and new_y >= 0 and new_y < dimensions[1]):
            if garden[new_y][new_x].upper() != plant:
                    perimeter += 1
        else:
             perimeter += 1
    return perimeter

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    for y, row in enumerate(input.read()[0:-1].split("\n")):
        garden.append([x for x in row])
    dimensions = (len(garden[0]), y+1)

for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        if garden[y][x] == garden[y][x].upper():
            [area, perimeter] = measure_plot(x, y)
            prices.append(area * perimeter)

print('Result = ', sum(prices))