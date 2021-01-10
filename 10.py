#!/bin/python3

def get_input():
    with open('./input/10.txt') as f: 
        return sorted(list(map(int, f.read().splitlines())))

def part_1(data):
    diff_1 = 1 if data[0] == 1 else 0
    diff_3 = 0 if data[0] == 3 else 0
    
    for i in range(1, len(data)):
        if data[i] - data[i - 1] == 3: diff_3 += 1
        if data[i] - data[i - 1] == 1: diff_1 += 1

    return diff_1 * (diff_3 + 1)
    
input = get_input()
print(part_1(input))
