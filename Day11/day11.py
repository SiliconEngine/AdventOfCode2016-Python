#!/usr/bin/python
"""Advent of Code 2016, Day 11, Part 1 and Part 2

https://adventofcode.com/2016/day/11

We have four floors of a factor for which we have to move "generator" and
"microchips" to the top floor using an elevator. Rules:

1) An elevator move must take at least one item, and not more than two.
2) A type of microchip can never be on the same floor as a different generator,
    unless its own generator is also on the floor.

Part 1 compute the least number of moves to get all items on the fourth floor.
Part 2 adds four new items (two generators and two microchips).

Note that the items are abbreviated to their first letter plus M or G.

It uses the Dijkstra algorithm. The simple implementation takes about 6.5 minutes, but
an optimization reduces both parts to about 850ms, but is not general (see below).

See floors.dat for full data.

Author: Tim Behrendsen
"""

import re, heapq
from collections import defaultdict

fn = 'test.dat'
fn = 'floors.dat'

# Test if particular floor is valid
def floor_valid(items):
    # If there's any generator, need to see if there's a microchip without
    # its corresponding generator
    if not any(f[1] == 'G' for f in items):
        return True
    return not any(f"{i[0]}G" not in items for i in items if i[1] == 'M')

"""
Create key for distance array, two versions.
The simple version uses a key based on the total state of the elevator floors. This will
work for all configurations.

The fast version uses uses counts of "pairs", "single generators" and "single microchips".
This works because item pairs are full interchangeable (an elevator state just with different
pairs in the same places is the same problem), so if we already have an equivalent state
with a better distance, we don't have to do an equivalent path with a worse one.

This isn't general, because we just have a count of the single generators and single
microchips. Those won't be interchangeable because it depends on where the corresponding
generator to each chip is located. But the fast version does give the right result for
the puzzle, and in only 850ms.
"""

# Simple and straightforward, but slow, version of mk_key(). This will work for all inputs.
mk_key_slow = lambda node: (node[0], tuple(tuple(sorted(f)) for f in node[1]))

# Faster version returns tuple of tuples, each with (number of pairs, number of G, number of M).
# This may not work for some inputs.
def mk_key(node):
    fcounts = []
    for f in node[1]:
        a = list(f)
        counts = [0, 0, 0]
        while a:
            i = a.pop()
            opp = i[0] + ('M' if i[1] == 'G' else 'G')
            if opp in a:
                a.remove(opp)
                counts[0] += 1      # New pair
            else:
                counts[1 if i[1] == 'G' else 2] += 1    # Single M or G

        fcounts.append(tuple(counts))
    return (node[0], tuple(fcounts))

# Find optimal path in graph using Dijkstra
def find_path(floors):
    # Dictionary to hold the shortest distances to each node
    distances = defaultdict(lambda: 999999)
    total_objects = sum(len(f) for f in floors)

    #  dist, floor#, floor state
    pq = [(0, (0, [ set(f) for f in floors ]))]

    while pq:
        # Get the node with the smallest distance
        dist, node = heapq.heappop(pq)
        if dist > distances[mk_key(node)]:
            continue                # See if stale (need for Python Dijkstra)
        floor, floor_list = node

        # Check if reached end state
        if len(floor_list[3]) == total_objects:
            return dist

        # Build list of each neighbor of the current node
        new_moves = []
        for new_floor in (floor+1, floor-1):
            if 0 <= new_floor <= 3:
                f = list(floor_list[floor])
                for i1, item1 in enumerate(f):
                    # Move single item
                    new_moves.append([new_floor, [ item1 ]])

                    # Move pairs of items
                    for i2 in range(i1+1, len(f)):
                        item2 = f[i2]
                        new_moves.append([new_floor, [ item1, item2 ]])

        new_dist = dist+1
        for move in new_moves:
            new_floor, items = move
            # Construct new state from moving items
            work = [ f.copy() for f in floor_list ]
            for i in items:
                work[floor].discard(i)
                work[new_floor].add(i)

            # See if new floors are valid
            if floor_valid(work[floor]) and floor_valid(work[new_floor]):
                new_node = (new_floor, work)
                k = mk_key(new_node)
                if new_dist < distances[k]:
                    distances[k] = new_dist
                    heapq.heappush(pq, (new_dist, new_node))

floors = [ set() for i in range(4) ]
with open(fn, 'r') as file:
    for floor in range(0, 4):
        contents = re.findall(r'(([\w-]+) (generator|microchip))', file.readline())
        # Input data is conveniently named to have unique first letters.
        for c in contents:
            floors[floor].add(c[1][0].upper() + c[2][0].upper())

min_dist = find_path(floors)
print(f"Part 1 is {min_dist}")

# For part 2, add in the extra items
for i in ('EG', 'EM', 'DG', 'DM'):
    floors[0].add(i)
min_dist = find_path(floors)
print(f"Part 2 is {min_dist}")
