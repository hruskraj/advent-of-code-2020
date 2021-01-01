#!/bin/python3

def get_input():
    with open('./input/1.txt') as f:
        return list(map(int, f.read().splitlines()))
    
def solve(numbers, count, sum = 2020, product = 1):
    if count == 0 and sum == 0:
        print(product)
        return True
    elif count > 0 and sum > 0:
        for a in numbers:
            n2 = numbers.copy()
            n2.remove(a)
            if solve(n2, count - 1, sum - a, product * a):
                return True
    return False

input = get_input()
solve(input, 2)
solve(input, 3)
