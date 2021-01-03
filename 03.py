#!/bin/python3

def get_input():
    with open('./input/3.txt', 'r') as f:
        return f.read().splitlines()
        
def get_number_of_trees(rows, right, down):
    res = 0
    m = len(rows[0])
    j = right
        
    for i in range(down, len(rows), down):
        if rows[i][j] == '#': res += 1
        j = (j + right) % m
    
    return res
        
def part_2(input):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res = 1
    
    for slope in slopes:
        res *= get_number_of_trees(input, *slope)
        
    return res
    
input = get_input()
print(get_number_of_trees(input, 3, 1))
print(part_2(input))
