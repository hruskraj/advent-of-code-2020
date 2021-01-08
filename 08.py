#!/bin/python3

def get_input():
    with open('./input/8.txt') as f:
        rows = map(lambda instr: instr.split(), f.read().splitlines())
        return [(instr[0], int(instr[1])) for instr in rows]
    
def run_code(instructions):
    acc = 0
    i = 0
    visited = set()
    
    while i not in visited and i < len(instructions):
        visited.add(i)
        offset = 1
        
        if instructions[i][0] == 'acc':
            acc += instructions[i][1]
        elif instructions[i][0] == 'jmp':
            offset = instructions[i][1]
        
        i += offset
    
    return (acc, i == len(instructions))

def debug_code(instructions):
    for i in range(0, len(instructions)):
        if instructions[i][0] != 'acc':
            arg = instructions[i][1]
            instructions[i] = ('nop', arg) if instructions[i][0] == 'jmp' else ('jmp', arg)
            if run_code(instructions)[1]:
                return instructions
            instructions[i] = ('nop', arg) if instructions[i][0] == 'jmp' else ('jmp', arg)
    return False

input = get_input()
print(run_code(input)[0])
print(run_code(debug_code(input))[0])
