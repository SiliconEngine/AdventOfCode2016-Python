#!/usr/bin/python
"""Advent of Code 2016, Day 13, Part 1 and Part 2

https://adventofcode.com/2016/day/13

Calculate the shortest distance to a node in a maze. The maze is specified
by a given formula that determines if a node is a wall or open. Part 2
gives the number of nodes within 50 moves of the origin.

Author: Tim Behrendsen
"""

import heapq
from collections import defaultdict

fav_num = 1350

# Given method to determine wall or open space
def is_wall(x, y):
    return (x*x + 3*x + 2*x*y + y + y*y + fav_num).bit_count() & 1

# Find optimal path in graph using Dijkstra
def find_path(end_x, end_y):
    # Dictionary to hold the shortest distances to each node
    distances = defaultdict(lambda: 999999)

    # Start coordinates
    pq = [(0, (1, 1))]

    while pq:
        # Get the node with the smallest distance
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue                # See if stale (need for Python Dijkstra)
        cur_x, cur_y = node

        # Check if reached end location
        if node == (end_x, end_y):
            return distances

        # Add each valid neighbor of the current node
        new_dist = dist+1
        for move in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = cur_x+move[0], cur_y+move[1]
            if new_x >= 0 and new_y >= 0 and not is_wall(new_x, new_y):
                new_node = (new_x, new_y)
                if new_dist < distances[new_node]:
                    distances[new_node] = new_dist
                    heapq.heappush(pq, (new_dist, new_node))

distances = find_path(31, 39)
print(f"Part 1: {distances[(31, 39)]}")

# For part 2, Distance to 31, 39 is much more than 50, so we can use results from that.
print(f"Part 2: {sum(d <= 50 for d in distances.values())}")

