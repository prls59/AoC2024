import os, re

datafile = "input.txt"

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    memory = input.read()
    result = sum(map((lambda xy: int(xy[0]) * int(xy[1])), re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memory)))

print('Result = ', result)