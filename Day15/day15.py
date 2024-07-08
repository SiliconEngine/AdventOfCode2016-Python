#!/usr/bin/python
"""Advent of Code 2016, Day 15, Part 1 and Part 2

https://adventofcode.com/2016/day/15

Given a set of rotating discs with different numbers of slots, we want to
find how much time to wait before dropping a "capsule" so that it falls
through all the slots. Each disc is one second apart and it takes one second
to reach the first disc.

Part 2 adds an additional disc.

See discs.dat for full data.

Author: Tim Behrendsen
"""

import re
from itertools import count

fn = 'discs.dat'

def calc(discs):
    # Try different time intervals until all discs align at an offset of 1. The offset
    # comes from the disc index in the enumerate.
    for t in count(1):
        if not any(((w[1] + t + chk + 1) % w[0]) != 0 for chk, w in enumerate(discs)):
            return t

# Example: Disc #1 has 13 positions; at time=0, it is at position 11.
with open(fn, 'r') as file:
    discs = [ (int(m[1]), int(m[3])) for m in (re.findall(r'\d+', line) for line in file) ]

print(f"Part 1: {calc(discs)}")

discs.append((11, 0))
print(f"Part 2: {calc(discs)}")
