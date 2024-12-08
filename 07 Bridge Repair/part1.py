import os

DATAFILE = "input.txt"

def evaluate(target, left, right):
    x = right[0]
    if len(right) == 1:
        if left * x == target:
            return target
        else:
            return left + x
    else:
        rest = right[1:]
        if left * x <= target:
            result = evaluate(target, left * x, rest)
            if result == target:
                return target
            else:
                return evaluate(target, left + x, rest)
        else:
            return evaluate(target, left + x, rest)

calibration_result = 0

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    for line in input:
        equation = line[0:-1].split(': ')
        target = int(equation[0])
        values = [int(x) for x in equation[1].split()]
        if evaluate(target, values[0], values[1:]) == target:
            calibration_result += target

print('Result = ', calibration_result)