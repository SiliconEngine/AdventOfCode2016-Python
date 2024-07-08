#!/usr/bin/python
"""Advent of Code 2016, Day 20, Part 1 and Part 2

https://adventofcode.com/2016/day/20

Given a set of ranges of invalid integer IP addresses, for Part 1, figure out
the lowest valid address. For Part 2, figure out the total number of valid
addresses.

See ranges.dat for full data.

Author: Tim Behrendsen
"""

import time

start_time = time.time()
fn = 'ranges.dat'
highest = 4294967295

with open(fn, 'r') as file:
    ranges = [(int(a), int(b)) for a, b in (line.strip().split('-') for line in file)]

# Sort the ranges and combine overlaps as we go.
sort_range = sorted(ranges)
cur_low, cur_high, total, lowest = 0, 0, 0, None
for r in sort_range:
    if cur_high >= r[0]:
        cur_high = max(cur_high, r[1])
    else:
        if lowest == None:
            lowest = cur_high+1
        total += r[0]-cur_high-1
        cur_low, cur_high = r

total += highest - cur_high
interval = time.time() - start_time
print(f"Executed in {round(interval*1000000)} microseconds")
print(f"Part 1 is {lowest}")
print(f"Part 2 is {total}")
