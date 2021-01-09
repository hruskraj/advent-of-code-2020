#!/bin/python3

def get_input():
    with open('./input/9.txt') as f:
        return list(map(int, f.read().splitlines()))

def get_sums(data, start, preamble = 25):
    res = []
    
    for i in range(0, preamble):
        for j in range(i + 1, preamble):
            res.append(data[start + i] + data[start + j])
    
    return res


def part_1(data, preamble = 25):
    for i in range(25, len(data)):
        sums = get_sums(data, i - preamble, preamble)
        if data[i] not in sums:
            return data[i]
    return -1

def part_2(data, target):
    for i in range(0, len(data)):
        sum = 0
        minn = target
        maxx = 0
        for j in range(i, len(data)):
            sum += data[j]
            minn = min(minn, data[j])
            maxx = max(maxx, data[j])
            if sum == target:
                return minn + maxx
    
input = get_input()
weakness = part_1(input)
print(weakness)
print(part_2(input, weakness))
