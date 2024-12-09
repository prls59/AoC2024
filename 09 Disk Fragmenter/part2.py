import os

DATAFILE = "input.txt"

files = {}
spaces = []

def defrag(file_range, space_range_list):
    file_from = file_range[0]
    file_to = file_range[1]
    file_length = file_to - file_from + 1
    for n in range(len(space_range_list)):
        space_range = space_range_list[n]
        if space_range[0] < file_from:
            space_length = space_range[1] - space_range[0] + 1
            if space_length >= file_length:
                file_range[:] = [space_range[0], space_range[0] + file_length - 1]
                if space_length == file_length:
                    space_range_list[:] = space_range_list[0:n] + space_range_list[n+1:]
                else:
                    space_range_list[:] = space_range_list[0:n] + [[space_range[0] + file_length, space_range[1]]] + space_range_list[n+1:]
                break
        else:
            break

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    disk_map = input.read()[:-1]

file_count = 0
start_block = 0
file_entry = True
for n in range(len(disk_map)):
    end_block = start_block + int(disk_map[n]) - 1
    if file_entry:
        files[file_count] = [start_block, end_block]
        file_count += 1
    elif end_block >= start_block:
        spaces.append([start_block, end_block])
    start_block = end_block + 1
    file_entry = not file_entry

for file_id in range(file_count - 1, -1, -1):
    defrag(files[file_id], spaces)

checksum = 0
for file_id, block_range in files.items():
    if file_id != 0:
        for block_no in range(block_range[0], block_range[1] + 1):
            checksum += file_id * block_no

print('Result = ', checksum)