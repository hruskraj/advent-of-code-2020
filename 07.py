#!/bin/python3

def get_input():
    res = {}
    with open('./input/7.txt') as f:
        for rule in map(lambda x: x.split(), f.read().splitlines()):
            content = []
            if rule[4] != 'no':
                i = 4
                while True:
                    content.append((int(rule[i]), rule[i + 1] + " " + rule[i + 2]))
                    if rule[i + 3][-1:] == '.': break
                    i += 4
            res[rule[0] + " " + rule[1]] = content
    return res

def number_of_required_bags(bags, current):
    res = 0
    for el in bags[current]:
        res += el[0] + el[0] * number_of_required_bags(bags, el[1])
    return res

def number_of_outer_bags(bags, b = 'shiny gold'):
    is_present = {}
    
    def contains(current, target):
        if current in is_present:
            return is_present[current]
        if target in map(lambda x: x[1], bags[current]):
            is_present[current] = True
            return True
        for bag in map(lambda x: x[1], bags[current]):
            if contains(bag, target):
                is_present[current] = True
                return True
        is_present[current] = False
        return False
    
    for bag in bags:
        contains(bag, b)
    return len([x for x in is_present if is_present[x]])
    

bags = get_input()
print(number_of_outer_bags(bags))
print(number_of_required_bags(bags, 'shiny gold'))
