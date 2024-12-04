import os

datafile = "input.txt"

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    rows = input.read()[0:-1].split("\n")

total_rows = len(rows)
total_cols = len(rows[0])

valid_pairs = ["MS","SM"]
centre = "A"

occurrences = 0

for row_num in range(1, total_rows - 1):
    col_num = rows[row_num][1:-1].find(centre) + 1
    while col_num >= 0:
        if (rows[row_num - 1][col_num - 1] + rows[row_num + 1][col_num + 1] in valid_pairs
            and rows[row_num - 1][col_num + 1] + rows[row_num + 1][col_num - 1] in valid_pairs):
            occurrences += 1
        col_num = rows[row_num][:-1].find(centre, col_num + 1)

print('Result = ', occurrences)