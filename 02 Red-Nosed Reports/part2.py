import os

datafile = "input.txt"

NOT_FOUND = -1
MIN_DIFF = 1
MAX_DIFF = 3

def sign(diff):
    x = 0
    if diff > 0:
        x = 1
    elif diff < 0:
        x = -1
    return x

def bad_level(levels):
    bad = NOT_FOUND
    for n in range(len(levels) - 1):
        diff = levels[n] - levels[n+1]
        if n == 0:
            gradient = sign(diff)
        if abs(diff) < MIN_DIFF or abs(diff) > MAX_DIFF or sign(diff) != gradient:
            bad = n
            break
    return bad

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    safe_count = 0
    levels = []
    for report in input:
        levels = [int(x) for x in report[0:-1].split()]
        bad = bad_level(levels)
        # check if safe, or safe without implicated level, or without the previous level
        # or without the next...
        if (bad == NOT_FOUND
            or bad_level(levels[:bad]+levels[bad+1:]) == NOT_FOUND
            or (bad > 0 and bad_level(levels[:bad-1]+levels[bad:]) == NOT_FOUND)
            or (bad < len(levels) - 1 and bad_level(levels[:bad+1]+levels[bad+2:]) == NOT_FOUND)):
            safe_count += 1

print('Result = ', safe_count)