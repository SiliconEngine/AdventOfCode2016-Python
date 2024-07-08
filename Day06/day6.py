#!/usr/bin/python
"""Advent of Code 2016, Day 6, Part 1 and Part 2

https://adventofcode.com/2016/day/6

Given a list of words, for Part 1, construct a word where each letter is the most frequent
letter in the column of the list. Part 2 is the least frequent letter in the column.

See path.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict

fn = 'test.dat'
fn = 'message.dat'

with open(fn, 'r') as file:
    msgs = [ line.strip() for line in file ]

# Add up letter frequency for each column
freq = [ defaultdict(int) for i in range(len(msgs[0])) ]
for m in msgs:
    for i, c in enumerate(m):
        freq[i][c] += 1

# Sort the frequences and take the most-common or least-common
msg1, msg2 = [], []
for f in freq:
    a = sorted([ (count, c) for c, count in f.items() ])
    msg1.append(a[-1][1])
    msg2.append(a[0][1])

print(f"Part 1: {''.join(msg1)}")
print(f"Part 2: {''.join(msg2)}")
