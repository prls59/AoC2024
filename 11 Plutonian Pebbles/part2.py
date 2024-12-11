import os

DATAFILE = "input.txt"

def blink(stones):
    new_stones = {}
    for engraving, count in stones.items():
        num_digits = len(str(engraving))
        if engraving == 0:
            new_stones[1] = new_stones.get(1, 0) + count
        elif num_digits % 2 == 0:
            num1 = int(str(engraving)[:int(num_digits/2)])
            num2 = int(str(engraving)[int(num_digits/2):])
            new_stones[num1] = new_stones.get(num1, 0) + count
            new_stones[num2] = new_stones.get(num2, 0) + count
        else:
            new_stones[engraving * 2024] = new_stones.get(engraving * 2024, 0) + count
    return new_stones

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    line = input.read()[:-1]

stones = {}

for stone in line.split():
    stones[int(stone)] = stones.get(int(stone), 0) + 1

for n in range(25):
    stones = blink(stones)

print('Part 1 = ', sum(stones.values()))

for n in range(50):
    stones = blink(stones)

print('Part 2 = ', sum(stones.values()))