import os

DATAFILE = "input.txt"

# Registers
A = 0
B = 1
C = 2

# Opcodes
ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

def run(program, ptr, register, output):
    opcode = program[ptr]
    operand = program[ptr + 1]
    next_ptr = ptr + 2
    if opcode == ADV:
        register[A] = register[A] // 2 ** combo(operand, register)
    elif opcode == BXL:
        register[B] = register[B] ^ operand
    elif opcode == BST:
        register[B] = combo(operand, register) % 8
    elif opcode == JNZ:
        if register[A] != 0:
            next_ptr = operand
    elif opcode == BXC:
        register[B] = register[B] ^ register[C]
    elif opcode == OUT:
        output.append(combo(operand, register) % 8)
    elif opcode == BDV:
        register[B] = register[A] // 2 ** combo(operand, register)
    elif opcode == CDV:
        register[C] = register[A] // 2 ** combo(operand, register)
    return next_ptr

def combo(operand, register):
    if operand < 4:
        return operand
    elif operand < 7:
        return register[operand - 4]
    else:
        raise RuntimeError('Invalid combo operand: ' + str(operand))

register = []

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + DATAFILE) as input:
    for n in range(3):
        register.append(int(input.readline()[12:-1]))
    input.readline()
    program = [int(x) for x in input.readline()[9:-1].split(',')]

output = []
ptr = 0

while ptr < len(program):
    ptr = run(program, ptr, register, output)

print('Result = ', ','.join(map(str, output)))