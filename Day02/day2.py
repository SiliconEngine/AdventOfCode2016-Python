#!/usr/bin/python
"""Advent of Code 2016, Day 2, Part 1 and Part 2

https://adventofcode.com/2016/day/2

The data is a path around a keypad, which we need to follow to produce an
entry code. Part 1 is a simple number grid. Part 2 is a more complex grid.

See doc.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'doc.dat'

def gen_code(instr, grid):
    # Find coordinates of '5'
    x, y = next((x, y) for y, line in enumerate(grid) for x, c in enumerate(grid) if grid[y][x] == '5')
    len_x, len_y = len(grid[0])-1, len(grid)-1
    moves = { 'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0) }

    for line in instr:
        for d in line:
            new_x, new_y = x + moves[d][0], y + moves[d][1]
            # Ignore move if invalid
            if 0 <= new_x <= len_x and 0 <= new_y <= len_y and grid[new_y][new_x] != '.':
                x, y = new_x, new_y
        yield grid[y][x]

with open(fn, 'r') as file:
    instr = [ line.strip() for line in file ]

grid = [ list('123'), list('456'), list('789') ]
gen = gen_code(instr, grid)
print(f"Part 1 is {''.join(c for c in gen)}")

grid = [ list('..1..'), list('.234.'), list('56789'), list('.ABC.'), list('..D..') ]
gen = gen_code(instr, grid)
print(f"Part 2 is {''.join(c for c in gen)}")
