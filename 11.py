#!/bin/python3

import copy

def get_input():
    with open('./input/11.txt', 'r') as f:
        return list(map(list, f.read().splitlines()))

def is_in_range(i, j, data):
    return 0 <= i < len(data) and 0 <= j < len(data[0])
   
def get_number_of_adjacent(i, j, data, c = 'L'):
    cnt = 0
    for e in [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (1, -1), (1, 1)]:
        if is_in_range(i + e[0], j + e[1], data) and data[i + e[0]][j + e[1]] == c:
            cnt += 1
    return cnt

def get_number_of_adjacent_extended(i, j, data, c = 'L'):
    cnt = 0
    for e in [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (1, -1), (1, 1)]:
        a = i + e[0]
        b = j + e[1]
        while is_in_range(a, b, data):
            if data[a][b] != '.':
                cnt += 1 if data[a][b] == c else 0
                break
            a += e[0]
            b += e[1]

    return cnt

def simulate(data, threshold, visibility_method):
    k = 0
    data_k = copy.copy(data)
    change = True
    
    while change:
        data_l = copy.deepcopy(data_k)
        change = False
        k += 1

        for i in range(0, len(data)):
            for j in range(0, len(data[0])):
                if data_k[i][j] == 'L' and visibility_method(i, j, data_k, '#') == 0:
                    data_l[i][j] = '#'
                    change = True
                elif data_k[i][j] == '#' and visibility_method(i, j, data_k, '#') >= threshold:
                    data_l[i][j] = 'L'
                    change = True
        data_k = data_l
    return sum(map(lambda x: x.count('#'), data_k))

input = get_input()
print(simulate(input, 4, get_number_of_adjacent))
print(simulate(input, 5, get_number_of_adjacent_extended))
