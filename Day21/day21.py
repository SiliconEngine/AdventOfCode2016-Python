#!/usr/bin/python
"""Advent of Code 2016, Day 21, Part 1 and Part 2

https://adventofcode.com/2016/day/21

We're given a list of string manipulation instructions. For Part 1, we apply the
various manipulations to a "password" and produce the encoded result. For Part 2,
we have to reverse the moves and turn an encoded result back into a password.

Reversing the instruction we're mostly straightforward, with the exception of one
that had complicated rules ("rotate based on position of letter x"). That one
required building a table of reverse rotations and adding a special instruction
for it.

See moves.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'moves.dat'
start_pwd = 'abcdefgh'
scrambled = 'fbgdceah'

# Execute moves on password
def process(pwd, moves):
    work = list(pwd)

    for m in moves:
        if a := re.findall(r'swap position (\d+) with position (\d+)', m):
            pos1, pos2 = map(int, a[0])
            work[pos1], work[pos2] = work[pos2], work[pos1]

        elif a := re.findall(r'swap letter (.) with letter (.)', m):
            l1, l2 = a[0]
            pos1, pos2 = work.index(l1), work.index(l2)
            work[pos1], work[pos2] = l2, l1

        elif a := re.findall('reverse positions (\d+) through (\d+)', m):
            pos1, pos2 = map(int, a[0])
            work[pos1:pos2+1] = reversed(work[pos1:pos2+1])

        elif a := re.findall(r'rotate left (\d+) step', m):
            steps = int(a[0][0])
            work = work[steps:] + work[0:steps]

        elif a := re.findall(r'rotate right (\d+) step', m):
            steps = int(a[0][0])
            work = work[-steps:] + work[0:-steps]

        elif a := re.findall(r'move position (\d+) to position (\d+)', m):
            f, t = map(int, a[0])
            c = work.pop(f)
            work.insert(t, c)

        elif a := re.findall(r'rotate based on position of letter (.)', m):
            pos = work.index(a[0][0])
            steps = (pos + 1 + (1 if pos >= 4 else 0)) % len(work)
            work = work[-steps:] + work[0:-steps]

        elif a := re.findall(r'special reverse rotate letter (.)', m):
            pos = work.index(a[0][0])
            steps = { 1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 0, 0: 1 }[pos]
            work = work[steps:] + work[0:steps]

    return ''.join(work)

# Generate the opposite transformation for a move
def reverse_move(m):
    if a := re.findall(r'swap position (\d+) with position (\d+)', m):
        return f"swap position {a[0][1]} with position {a[0][0]}"
    elif a := re.findall(r'swap letter (.) with letter (.)', m):
        return f"swap letter {a[0][1]} with letter {a[0][0]}"
    elif a := re.findall('reverse positions (\d+) through (\d+)', m):
        return m
    elif a := re.findall(r'rotate left (\d+) step', m):
        return m.replace('left', 'right')
    elif a := re.findall(r'rotate right (\d+) step', m):
        return m.replace('right', 'left')
    elif a := re.findall(r'move position (\d+) to position (\d+)', m):
        return f"move position {a[0][1]} to position {a[0][0]}"
    elif a := re.findall(r'rotate based on position of letter (.)', m):
        return f"special reverse rotate letter {a[0][0]}"

moves = [ line.strip() for line in open(fn, 'r') ]
print(f"Part 1: {process(start_pwd, moves)}")
print(f"Part 2: {process(scrambled, [reverse_move(m) for m in reversed(moves)])}")
