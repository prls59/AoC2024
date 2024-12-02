import os

datafile = "input.txt"

safe_count = 0
min_diff = 1
max_diff = 3
levels = []

def sign(diff):
    x = 0
    if diff > 0:
        x = 1
    elif diff < 0:
        x = -1
    return x

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    for report in input:
        levels = [int(x) for x in report[0:-1].split()]
        gradient = 0
        safe = True
        for n in range(len(levels) - 1):
            diff = levels[n] - levels[n+1]
            if n == 0:
                gradient = sign(diff)
            safe = abs(diff) >= min_diff and abs(diff) <= max_diff and sign(diff) == gradient
            if not safe:
                break
        if safe:
            safe_count += 1

print('Result = ', safe_count)