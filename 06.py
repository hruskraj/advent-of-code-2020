#!/bin/python3

def get_input():
    with open('./input/6.txt', 'r') as f:
        return list(map(lambda x: x.split(), f.read().split('\n\n')))

def count_answers(group, is_union = True):
    if not group:
        return 0
    res = set() if is_union else set(group.pop(0))
    for person in group:
        s = set()
        for answer in person:
            s.add(answer)
        res = res.union(s) if is_union else res.intersection(s)
    return len(res)
    
groups = get_input()
print(sum(map(lambda group: count_answers(group, True), groups)))
print(sum(map(lambda group: count_answers(group, False), groups)))
