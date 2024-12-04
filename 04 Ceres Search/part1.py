import os

datafile = "input.txt"

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    rows = input.read()[0:-1].split("\n")

total_rows = len(rows)
total_cols = len(rows[0])

search_word = "XMAS"
word_length = len(search_word)

occurrences = 0

for row_num in range(total_rows):
    col_num = rows[row_num].find(search_word[0])
    while col_num >= 0:
        for delta_x in range(-1, 2):
            for delta_y in range(-1, 2):
                if ((delta_x == 0 and delta_y == 0)
                    or (delta_x < 0 and col_num < word_length - 1)
                    or (delta_x > 0 and col_num > total_cols - word_length)
                    or (delta_y < 0 and row_num < word_length - 1)
                    or (delta_y > 0 and row_num > total_rows - word_length)):
                    continue
                found_one = True
                for n in range(1, word_length):
                    if rows[row_num + delta_y * n][col_num + delta_x * n] != search_word[n]:
                        found_one = False
                        break
                if found_one:
                    occurrences += 1
        col_num = rows[row_num].find(search_word[0], col_num + 1)

print('Result = ', occurrences)