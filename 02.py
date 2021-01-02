#!/bin/python3

def get_input():
    with open('./input/2.txt', 'r') as f:
        l = map(lambda x: tuple(x.split()), f.readlines())
        return list(map(lambda x: (tuple(map(int, x[0].split('-'))), x[1][0], x[2]), l))
        
def is_valid_1(range, letter, password):
    cnt = password.count(letter)
    return cnt >= range[0] and cnt <= range[1]

def is_valid_2(range, letter, password):
    return (password[range[0] - 1] == letter or password[range[1] - 1] == letter) and password[range[0] - 1] != password[range[1] - 1]

def solve(input, is_valid):
    return len([el for el in input if is_valid(*el)])
    
input = get_input()
print(solve(input, is_valid_1))
print(solve(input, is_valid_2))
