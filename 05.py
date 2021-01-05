#!/bin/python3

def get_input():
    with open('./input/5.txt') as f:
        return f.read().splitlines()

def get_num(seq, high_char, high):
    low = 0
    for char in seq:
        if char == high_char:
            low = low + (high - low) // 2 + 1
        else:
            high = low + (high - low) // 2
        
    return low

def decode_seat(seat):
    return (get_num(seat[:-3], 'B', 127), get_num(seat[-3:], 'R', 7))
    
def get_id(seat):
    return seat[0] * 8 + seat[1]

def get_highest_id(seats):
    return max(map(lambda seat: get_id(decode_seat(seat)), seats))

def get_missing_id(seats):
    decoded_seats = list(map(lambda seat: get_id(decode_seat(seat)), seats))
    
    for id in range(min(decoded_seats), max(decoded_seats)):
        if not id in decoded_seats:
            return id

input = get_input()
print(get_highest_id(input))
print(get_missing_id(input))
