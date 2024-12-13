import os, re

#
# NB. Shonky -- see part 2 code for better solution.
#

DATAFILE = "input.txt"

MAX_PRESSES = 100
X = 0
Y = 1
A_TOKENS = 3
B_TOKENS = 1

def fewest_tokens(button_a, button_b, prize):
    fewest = 0
    min_a_presses = max(int((prize[X] - MAX_PRESSES * button_b[X]) / button_a[X]),
                        int((prize[Y] - MAX_PRESSES * button_b[Y]) / button_a[Y]),
                        0)
    min_b_presses = max(int((prize[X] - MAX_PRESSES * button_a[X]) / button_b[X]),
                        int((prize[Y] - MAX_PRESSES * button_a[Y]) / button_b[Y]),
                        0)
    max_a_presses = min(int(prize[X] / button_a[X]), int(prize[Y] / button_a[Y]), MAX_PRESSES)
    max_b_presses = min(int(prize[X] / button_b[X]), int(prize[Y] / button_b[Y]), MAX_PRESSES)
    if min_a_presses > max_a_presses or min_b_presses > max_b_presses:
        return 0
    else:
        for a in range(min_a_presses, max_a_presses + 1):
            b_modulo_x = (prize[X] - button_a[X] * a) % button_b[X]
            b_modulo_y = (prize[Y] - button_a[Y] * a) % button_b[Y]
            b_x = int((prize[X] - button_a[X] * a) / button_b[X])
            b_y = int((prize[Y] - button_a[Y] * a) / button_b[Y])
            if b_modulo_x == 0 and b_modulo_y == 0 and b_x == b_y and b_x <= max_b_presses:
                if fewest == 0 or fewest > a * A_TOKENS + b_x * B_TOKENS:
                    fewest = a * A_TOKENS + b_x * B_TOKENS
        return fewest

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    lines = input.readlines()

total_tokens = 0

for n in range(0 ,len(lines), 4):
    button_a = [(int(x), int(y)) for (x, y) in re.findall(r'X\+(\d+), Y\+(\d+)', lines[n])]
    button_b = [(int(x), int(y)) for (x, y) in re.findall(r'X\+(\d+), Y\+(\d+)', lines[n+1])]
    prize = [(int(x), int(y)) for (x, y) in re.findall(r'X=(\d+), Y=(\d+)', lines[n+2])]
    total_tokens += fewest_tokens(button_a[0], button_b[0], prize[0])

print('Result = ', total_tokens)