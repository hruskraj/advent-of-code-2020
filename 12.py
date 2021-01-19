#!/bin/python3

def get_input():
    with open('./input/12.txt', 'r') as f:
        return list(map(lambda el: (el[0], int(el[1:])), f.read().splitlines()))
        
def move(direction, length, x, y):
    if direction == 'N':
        y += length
    elif direction == 'S':
        y -= length
    elif direction == 'E':
        x += length
    elif direction == 'W':
        x -= length
    return x, y

def rotate(direction, degrees, facing):
    if direction == 'L':
        degrees = 360 - degrees
    pos = ['E', 'S', 'W', 'N']
    return pos[(pos.index(facing) + int(degrees / 90)) % 4]

def part_1(input, facing = 'E', x = 0, y = 0):
    for m in input:
        if m[0] in ['N', 'S', 'E', 'W']:
            x, y = move(m[0], m[1], x, y)
        elif m[0] == 'F':
            x, y = move(facing, m[1], x, y)
        else:
            facing = rotate(m[0], m[1], facing)
    return abs(x) + abs(y)

def rotate_waypoint(direction, degrees, wp_x, wp_y):
    if direction == 'L':
        degrees = 360 - degrees
    for i in range(0, int(degrees / 90)):
        wp_x, wp_y = wp_y, -wp_x
    return wp_x, wp_y

def part_2(input, s_x = 0, s_y = 0, wp_x = 10, wp_y = 1):
    for m in input:
        if m[0] in ['N', 'S', 'E', 'W']:
            wp_x, wp_y = move(m[0], m[1], wp_x, wp_y)
        elif m[0] in ['R', 'L']:
            wp_x, wp_y = rotate_waypoint(m[0], m[1], wp_x, wp_y)
        else:
            s_x += wp_x * m[1]
            s_y += wp_y * m[1]

    return abs(s_x) + abs(s_y)
    
input = get_input()
print(part_1(input))
print(part_2(input))
