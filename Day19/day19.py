#!/usr/bin/python
"""Advent of Code 2016, Day 19, Part 1 and Part 2

https://adventofcode.com/2016/day/19

A group of elves sits in a circle, each with a Christmas present. On each elf turn,
they take the presents from another elf, and the elf without presents is removed
from the circle. Find which elf ends up with all the presents.

In Part 1, the current elf takes the presents from the elf on their immediate left
(facing the circle). In Part 2, the current elf takes the presents from the elf across
the circle.

This puzzle was all about efficient data structures. Part 1 uses "deque" from the
Python standard library. Part 2 uses a single-linked ringer buffer. Most of the run
time is spent initializing the data structures.

There's likely also a formula that can just calculate the final result, but I didn't
go looking for that.

Author: Tim Behrendsen
"""

from collections import deque

elves = 3017957
# Used by both parts
init_data = list(range(1, elves+1))

def part1():
    circle = deque(init_data)
    while len(circle) > 1:
        circle.rotate(-1)
        circle.popleft()

    return circle[0]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SingleLinkedRing:
    def __init__(self, items):
        self.head = None
        last_node = None
        for item in items:
            node = Node(item)
            if self.head == None:
                self.head = node
            if last_node != None:
                last_node.next = node
                node.prev = last_node
            last_node = node
        last_node.next = self.head
        self.head.prev = last_node
        self.size = len(items)

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

def part2():
    circle = SingleLinkedRing(init_data)
    cur_elf = circle.head
    cross_elf = circle.head
    for i in range(elves // 2):
        cross_elf = cross_elf.next

    while circle.size > 1:
        cur_elf = cur_elf.next

        # As we delete, on even sizes, we move an extra one. This has the effect
        # of keeping the cross-ways elf always across from cur_elf.
        circle.delete(cross_elf)
        cross_elf = cross_elf.next if circle.size % 2 else cross_elf.next.next

    return cur_elf.data

print(f"Part 1 is {part1()}")
print(f"Part 2 is {part2()}")
