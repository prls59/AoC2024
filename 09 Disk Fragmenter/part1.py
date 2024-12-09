import os
from collections import defaultdict

DATAFILE = "input.txt"

files = defaultdict(list)
spaces = []

def defrag(file_range, space_range_list):
    new_blocks = []
    file_from = file_range[0]
    file_to = file_range[1]
    defragging = True
    while defragging:
        if len(space_range_list) == 0 or space_range_list[0][0] > file_range[1]:
            defragging = False
        else:
            space_range = space_range_list[0]
            space_length = space_range[1] - space_range[0] + 1
            file_length = file_to - file_from + 1
            if space_length > file_length:
                new_blocks.append([space_range[0], space_range[0] + file_length - 1])
                space_range_list[:] = [[space_range[0] + file_length, space_range[1]]] + space_range_list[1:]
                defragging = False
            else:
                if (len(space_range_list) == 1 or space_length == file_length
                    or space_range[1] + 1 == file_from):
                    new_blocks.append([space_range[0], space_range[0] + file_length - 1])
                    defragging = False
                else:
                    new_blocks.append([space_range[0], space_range[1]])
                    file_to -= space_length
                space_range_list[:] = space_range_list[1:]
    return new_blocks

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    disk_map = input.read()[:-1]

file_count = 0
start_block = 0
file_entry = True
for n in range(len(disk_map)):
    end_block = start_block + int(disk_map[n]) - 1
    if file_entry:
        files[file_count].append([start_block, end_block])
        file_count += 1
    elif end_block >= start_block:
        spaces.append([start_block, end_block])
    start_block = end_block + 1
    file_entry = not file_entry

for file_id in range(file_count - 1, -1, -1):
    new_blocks = defrag(files[file_id][0], spaces)
    if len(new_blocks) > 0 and files[file_id] != new_blocks:
        files[file_id] = new_blocks
    else:
        break

checksum = 0
for file_id, block_list in files.items():
    if file_id != 0:
        for block_range in block_list:
            for block_no in range(block_range[0], block_range[1] + 1):
                checksum += file_id * block_no

print('Result = ', checksum)