import os, re

datafile = "input.txt"

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    memory = input.read()
    mem_len = len(memory)
    start = 0
    end = memory.find("don't()")
    if end == -1:
        end = mem_len
    result = 0
    while start < end:
        result += sum(map((lambda xy: int(xy[0]) * int(xy[1])), re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memory[start:end])))
        start = memory.find("do()",end)
        if start == -1:
            break
        end = memory.find("don't()",start)
        if end == -1:
            end = mem_len
print('Result = ', result)