#!/usr/bin/python
"""Advent of Code 2016, Day 22, Part 1 and (not) Part 2

https://adventofcode.com/2016/day/22

We're given a list of filesystems accessible through a network. We can move all files
from one "adjacent" filesystem to another. Part 1 figures out how many filesystems
can move their files to a different files with sufficient capacity.

It turns out that Part 2 can't be solved in a general way, and the intent was to
manually calculate the answer because of the example data was very specific. There
are ways to solve it limiting oneself to those assumptions.

See fs.dat for full data.

Author: Tim Behrendsen
"""

import re
import heapq
from collections import defaultdict

fn = 'fs.dat'
fn = 'test.dat'

def part1(fs_data):
    count = 0
    for ka, fs_a in fs_data.items():
        if fs_a['u'] == 0:
            continue
        for kb, fs_b in fs_data.items():
            if ka == kb:
                continue
            if fs_a['u'] <= fs_b['a']:
                count += 1

    return count

with open(fn, 'r') as file:
    fs_data = { }
    get_num = lambda s: int(s[:-1])
    for line in file:
        if line[0] == '/':
            (name, size, used, avail, use) = line.strip().split()
            x, y = map(int, re.findall('\d+', name))
            fs_data[(x, y)] = {'s': get_num(size), 'u': get_num(used), 'a': get_num(avail)}

print(f"Part 1 is {part1(fs_data)}")
