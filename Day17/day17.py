#!/usr/bin/python
"""Advent of Code 2016, Day 17, Part 1 and Part 2

https://adventofcode.com/2016/day/17

Navigate a maze and get the shortest (part 1) and longest (part 2) paths to the
end point. The wrinkle is that whether doors in a room are open or not is based
on the MD5 hash of a "passcode" and the prior directions of the path to the room.

Author: Tim Behrendsen
"""

from hashlib import md5

passcode = 'udskfozm'

# Do depth-first-search of all paths to get shortest and longest
longest, shortest, shortest_path = 0, 99999, None
q = [(0, 0, '')]
while q:
    cur_x, cur_y, path = q.pop()

    # Check if reached end location
    if (cur_x, cur_y) == (3, 3):
        if len(path) > longest:
            longest = len(path)
        elif len(path) < shortest:
            shortest, shortest_path = len(path), path
        continue

    # Add each valid neighbor of the current node
    doors = md5((passcode + path).encode('utf-8')).hexdigest()
    for idx, move in enumerate(((0, -1, 'U'), (0, 1, 'D'), (-1, 0, 'L'), (1, 0, 'R'))):
        if doors[idx] in 'bcdef':
            new_x, new_y, d = cur_x+move[0], cur_y+move[1], move[2]
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                q.append((new_x, new_y, path+d))

print(f"Part 1 is {shortest_path}")
print(f"Part 2 is {longest}")
