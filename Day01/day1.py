#!/usr/bin/python
"""Advent of Code 2016, Day 1, Part 1 and Part 2

https://adventofcode.com/2016/day/1

Given a list of right and left turns and distances, follow the path and
compute the taxi distance. Part 2 traces the entire path and figures out where
visits the same coordinates twice.

See path.dat for full data.

Author: Tim Behrendsen
"""

fn = 'path.dat'

DIR_N, DIR_E, DIR_S, DIR_W = 0, 1, 2, 3
moves = ((0, -1), (1, 0), (0, 1), (-1, 0))

# Follow the path and calculate taxi distance from origin
def part1(path):
    x, y, d = 0, 0, DIR_N
    for move in path:
        d = (d + (1 if move[0] == 'R' else -1)) % 4
        dist = int(move[1:])
        x, y = x + (moves[d][0] * dist), y + (moves[d][1] * dist)

    return abs(x)+abs(y)

# Follow the path and figure out first coordinates crossed twice.
def part2(path):
    x, y, d = 0, 0, DIR_N
    seen = set()
    for move in path:
        d = (d + (1 if move[0] == 'R' else -1)) % 4
        for i in range(int(move[1:])):
            x, y = x + moves[d][0], y + moves[d][1]
            if (x, y) in seen:
                return abs(x)+abs(y)
            seen.add((x, y))

with open(fn, 'r') as file:
    path = file.readline().strip().split(', ')

print(f"Part 1 is {part1(path)}")
print(f"Part 2 is {part2(path)}")
