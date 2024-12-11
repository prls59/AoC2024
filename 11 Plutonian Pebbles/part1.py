import os

DATAFILE = "input.txt"

def blink():
    curr_count = len(stones)
    for n in range(curr_count):
        engraving = stones[n]
        num_digits = len(str(engraving))
        if engraving == 0:
            stones[n] = 1
        elif num_digits % 2 == 0:
            stones[n] = int(str(engraving)[:int(num_digits/2)])
            stones.append(int(str(engraving)[int(num_digits/2):]))
        else:
            stones[n] = engraving * 2024

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    stones = [int(x) for x in input.read()[:-1].split()]

for n in range(25):
    blink()

print('Part 1 = ', len(stones))