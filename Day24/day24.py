#!/usr/bin/python
"""Advent of Code 2016, Day 24, Part 1 and Part 2

https://adventofcode.com/2016/day/24

We're given a maze of "HVAC ducts", with certain points marked with a series of
numbers. In Part 1, our task is to start at '0' and navigate the maze visiting
all the numbers, finding the length of the shortest path. In Part 2, we have to
navigate the same way, but end up at the origin.

Uses Breadth-First-Search where each node is coordinates + bitmap of visited numbers.
Part 1 and Part 2 could be combined by keeping an intermediate result of reaching
the final number, and the continuing until reaching the origin.

See hvac.dat for full data.

Author: Tim Behrendsen
"""

from collections import deque
import time

start_time = time.process_time()
fn = 'hvac.dat'

# Breadth-First-Search to find distance
def run(m):
    # Find '0', which is starting coordinates, and highest number used
    start_x, start_y = next((x, y) for y, row in enumerate(m) for x, c in enumerate(row) if c == '0')
    max_n = int(max(c for row in m for c in row if c.isdigit()))

    # Each node is the coordinates visited + bitmap of what numbers we've seen
    start_node = (start_x, start_y, 1)
    visited = set([start_node])
    q = deque([(0, start_node)])
    dist1 = None
    target = 2**(max_n+1) - 1               # Final bitmap of all numbers
    while q:
        dist, node = q.popleft()
        x, y, curset = node
        if curset == target:
            if dist1 == None:               # Found part 1, continue until back to origin
                dist1 = dist
            if (x, y) == (start_x, start_y):
                return dist1, dist

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = x + dx, y + dy
            c = m[new_y][new_x]
            if c != '#':
                # If a number, add it to the bitmap
                new_node = (new_x, new_y, curset | (1 << int(c)) if c.isdigit() else curset)
                if new_node not in visited:
                    q.append((dist+1, new_node))
                    visited.add(new_node)

m = [ line.strip() for line in open(fn, 'r') ]
print(f"Part 1, 2: {run(m)}")
print(f"Run time was {round(time.process_time() - start_time, 3)} secs")
