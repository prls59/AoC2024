import os, re

DATAFILE = "input.txt"

MAX_PRESSES = 100                   # part 1 only

NO_LIMIT = True                     # part 2: switch off MAX_PRESSES limit
CONVERSION_ERROR = 10000000000000   # part 2: unit conversion error for prize

X = 0
Y = 1
A_COST = 3
B_COST = 1

def count_tokens(button_a, button_b, prize):
    a = (prize[X] * button_b[Y] - prize[Y] * button_b[X]) / (button_b[Y] * button_a[X] - button_b[X] * button_a[Y])
    b = (prize[X] - a * button_a[X]) / button_b[X]
    if a == int(a) and b == int(b) and (NO_LIMIT or a <= MAX_PRESSES and b <= MAX_PRESSES):
        tokens = int(a) * A_COST + int(b) * B_COST
    else:
        tokens = 0
    return tokens

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    lines = input.readlines()

total_tokens = 0

for n in range(0 ,len(lines), 4):
    button_a = [(int(x), int(y)) for (x, y) in re.findall(r'X\+(\d+), Y\+(\d+)', lines[n])]
    button_b = [(int(x), int(y)) for (x, y) in re.findall(r'X\+(\d+), Y\+(\d+)', lines[n+1])]
    prize = [(int(x) + CONVERSION_ERROR, int(y) + CONVERSION_ERROR) for (x, y) in re.findall(r'X=(\d+), Y=(\d+)', lines[n+2])]
    total_tokens += count_tokens(button_a[0], button_b[0], prize[0])

print('Result = ', total_tokens)