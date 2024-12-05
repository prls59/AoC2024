import os
from collections import defaultdict

datafile = "input.txt"

rules = defaultdict(list)
middle_sum = 0

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    line = input.readline()[0:-1]
    while line != '':
        (before, after) = line.split('|')
        rules[int(before)].append(int(after))
        line = input.readline()[0:-1]

    line = input.readline()[0:-1]
    while line != '':
        pages = [int(x) for x in line.split(',')]
        valid = True
        for n in range(1, len(pages)):
            cur_page = pages[n]
            if cur_page in rules:
                afters = rules[cur_page]
                for m in range(n):
                    if pages[m] in afters:
                        valid = False
                        break
            else:
                continue
            if not valid:
                break
        if valid:
            middle_sum += pages[len(pages)//2]
        line = input.readline()[0:-1]
        
print('Result = ', middle_sum)