#!/usr/bin/python
"""Advent of Code 2016, Day 4, Part 1 and Part 2

https://adventofcode.com/2016/day/4

The input data is a list of "rooms" identified by a hash. Some of the rooms are
invalid, so step 1 counts the valid ones using the supplied method. Part 2 decodes
the rooms and finds the "North Pole Object Storage" room, which required scanning
the output and finding the correct phrase.

See rooms.dat for full data.

Author: Tim Behrendsen
"""

import re
from collections import defaultdict

fn = 'test.dat'
fn = 'rooms.dat'

with open(fn, 'r') as file:
    rooms = []
    for line in file:
        # Format: aaaaa-bbb-z-y-x-123[abxyz]
        m = re.findall(r'([a-z-]+)-(\d+)\[(\w+)\]', line)[0]
        rooms.append([ m[0].split('-'), int(m[1]), m[2] ])

total_valid = 0
for r in rooms:
    counts = defaultdict(int)
    for c in ''.join(r[0]):
        counts[c] += 1
    # Sort by count descending, then by alphabetic (ascending)
    order = sorted([ (n, c) for c, n in counts.items() ], key=lambda item: (-item[0], item[1]))
    # Get first five (or fewer if there are fewer)
    chk = ''.join(item[1] for i, item in enumerate(order) if i < 5)

    # Check if hash is valid
    if chk == r[2]:
        total_valid += r[1]

        # Valid, so decode and see if it's the northpole object storage
        s = [ c for c in ' '.join(r[0]) ]
        for i, c in ((i, c) for i, c in enumerate(s) if c != ' '):
            s[i] = chr(((ord(c)-ord('a') + r[1]) % 26) + ord('a'))
        if ''.join(s) == 'northpole object storage':
            part2 = r[1]

print(f"Part 1 is {total_valid}")
print(f"Part 2 is {part2}")
