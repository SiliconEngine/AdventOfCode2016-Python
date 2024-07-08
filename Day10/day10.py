#!/usr/bin/python
"""Advent of Code 2016, Day 10, Part 1 and Part 2

https://adventofcode.com/2016/day/10

The input is a list of bot rules, where they trade numbered "chips", and are eventually
put into a numbered output bin. Part 1: Figure out which bot compares value-61 chips with
value 17 chips. Part 2 is figuring out what chip numbers end up in output bins 0, 1, and 2.

See bots.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict
import re

fn = 'bots.dat'

with open(fn, 'r') as file:
    instrs = [ line.strip() for line in file ]

bots, outputs, target_bot = defaultdict(list), defaultdict(set), None

# First find bot initializations
for instr in filter(lambda i: i.startswith('value'), instrs):
    v, b = map(int, re.findall('\d+', instr))
    bots[b].append(v)

# Repeat rules until we get our results
while target_bot == None or sum(len(outputs[n]) != 0 for n in range(3)) < 3:
    for instr in filter(lambda i: i.startswith('bot'), instrs):
        bot, dest1, dest2 = map(int, re.findall('\d+', instr))
        types = re.findall('to (bot|output)', instr)
        if len(bots[bot]) >= 2:
            low, high = sorted(bots[bot])
            if low == 17 and high == 61:
                target_bot = bot

            for d, t, v in zip((dest1, dest2), types, (low, high)):
                if t != 'output':
                    bots[d].append(v)
                else:
                    outputs[d].add(v)
            bots[bot] = [ ]

print(f"Part 1: {target_bot}")
a, b, c = (next(iter(outputs[n])) for n in range(3))
print(f"Part 2: {a * b * c}")
