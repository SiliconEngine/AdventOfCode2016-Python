#!/usr/bin/python
"""Advent of Code 2016, Day 5, Part 1 and Part 2

https://adventofcode.com/2016/day/5

Given an md5-based password encoding scheme, decode a password based on a "door ID".
Part 1 and part 2 use a bit different algorithms

See path.dat for full data.

Author: Tim Behrendsen
"""

from hashlib import md5

door_id = 'abc'                 # Test from puzzle
door_id = 'ugkcyxxp'

# Part 1: Accumulate sixth digit when md5 starts with five zeroes.
# Part 2: Accumulate each digit where sixth digit specifies the position,
#     and the seventh digit is contents of that position.
pwd1, pwd2, idx, count = [], [ None ] * 8, 0, 0
while len(pwd1) < 8 or count < 8:
    h = md5((door_id + str(idx := idx+1)).encode('utf-8')).hexdigest()
    if h[0:5] == '00000':
        pwd1.append(h[5])               # Part 1
        if h[5].isdigit() and 0 <= int(h[5]) < 8 and pwd2[int(h[5])] == None:
            count += 1
            pwd2[int(h[5])] = h[6]      # Part 2

print(f"Part 1 is {''.join(pwd1[0:8])}")
print(f"Part 2 is {''.join(pwd2)}")
