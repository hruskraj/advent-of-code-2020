#!/bin/python3

def get_input():
    with open('./input/4.txt', 'r') as f:
        res = []
        for passport in map(lambda x: x.split(), f.read().split('\n\n')):
            d = {}
            for entry in passport:
                p = entry.split(':')
                d[p[0]] = p[1]
            res.append(d)
        return res

def has_required_fields(passport):
    return len(passport) == 8 or (len(passport) == 7 and not 'cid' in passport)

def is_valid_height(height):
    unit = height[-2:]
    h = height[:-2]
    if unit == 'cm':
        return h.isnumeric() and int(h) >= 150 and int(h) <= 193
    return h.isnumeric() and int(h) >= 59 and int(h) <= 76

def is_valid_hair_color(hcl):
    try:
        int(hcl[1:], 16)
        return hcl[0] == '#' and len(hcl) == 7
    except:
        return False
    
def has_valid_data(p):
    return p['byr'].isnumeric() and 1920 <= int(p['byr']) <= 2002 and \
           p['iyr'].isnumeric() and 2010 <= int(p['iyr']) <= 2020 and \
           p['eyr'].isnumeric() and 2020 <= int(p['eyr']) <= 2030 and \
           p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
           is_valid_hair_color(p['hcl']) and \
           is_valid_height(p['hgt']) and \
           len(p['pid']) == 9 and p['pid'].isnumeric()
        
passports = get_input()
valid_passports = [passport for passport in passports if has_required_fields(passport)]
print(len(valid_passports))
print(len([passport for passport in valid_passports if has_valid_data(passport)]))
