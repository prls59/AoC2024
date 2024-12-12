import os

DATAFILE = "input.txt"

STEPS = [(-1,0),(0,-1),(1,0),(0,1)]

garden = []

def plots_in_region(x, y):
    region = []
    region.append([x,y])
    garden[y][x] = garden[y][x].lower()
    for step in STEPS:
        new_x = x + step[0]
        new_y = y + step[1]
        if (new_x >= 0 and new_x < dimensions[0]
            and new_y >= 0 and new_y < dimensions[1]):
            if garden[new_y][new_x] == garden[y][x].upper():
                    region.extend(plots_in_region(new_x, new_y))
    return region

def count_region_sides(plot_list):
    num_sides = 0
    sorted_plots = sorted(plot_list, key=rowsfirst)
    visited_plots = []
    for plot in sorted_plots:
        num_sides += count_plot_sides(plot, visited_plots)
    return num_sides
    
def rowsfirst(plot):
    return 1000 * plot[1] + plot[0]

def count_plot_sides(plot, visited_plots):
    sides = 0
    visited_plots[:] = visited_plots + [plot]
    for step in STEPS:
        if new_side(plot, step, visited_plots):
            sides += 1
    return sides

def new_side(plot, step, visited_plots):
    new_x = plot[0] + step[0]
    new_y = plot[1] + step[1]
    if (new_x < 0 or new_x >= dimensions[0] or new_y < 0 or new_y >= dimensions[1]
        or garden[new_y][new_x].upper() != garden[plot[1]][plot[0]].upper()):
        # perimeter - now check either side...
        left_x = plot[0] + step[1]
        left_y = plot[1] + step[0]
        if (left_x >= 0 and left_x < dimensions[0] and left_y >= 0 and left_y < dimensions[1]
            and [left_x, left_y] in visited_plots
            and (left_x + step[0] < 0 or left_x + step[0] >= dimensions[0]
                or left_y + step[1] < 0 or left_y + step[1] >= dimensions[1]
                or garden[left_y + step[1]][left_x + step[0]].upper() != garden[plot[1]][plot[0]].upper())):
            return False
        else:
            right_x = plot[0] - step[1]
            right_y = plot[1] - step[0]
            if (right_x >= 0 and right_x < dimensions[0] and right_y >= 0 and right_y < dimensions[1]
                and [right_x, right_y] in visited_plots
                and (right_x + step[0] < 0 or right_x + step[0] >= dimensions[0]
                    or right_y + step[1] < 0 or right_y + step[1] >= dimensions[1]
                    or garden[right_y + step[1]][right_x + step[0]].upper() != garden[plot[1]][plot[0]].upper())):
                return False
            else:
                return True
    else:
        return False

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    for y, row in enumerate(input.read()[0:-1].split("\n")):
        garden.append([x for x in row])
    dimensions = (len(garden[0]), y + 1)

tot_price = 0

for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        if garden[y][x] == garden[y][x].upper():
            plot_list = plots_in_region(x, y)
            num_sides = count_region_sides(plot_list)
            tot_price += len(plot_list) * num_sides

print('Result = ', tot_price)