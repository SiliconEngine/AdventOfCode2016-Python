#!/usr/bin/python
"""Advent of Code 2016, Day 7, Part 1 and Part 2

https://adventofcode.com/2016/day/7

We're given a list of security patterns, each with letters outside of brackets, and
letters inside of brackets.

For Part 1, identify letters that are of pattern of [letter1][letter2][letter2][letter1]
that are contained outside of brackets, but don't have that pattern inside the brackets.

For Part 2, identify all [letter1][letter2][letter1] patterns outside brackets that are
also have [letter2][letter1][letter2] inside the brackets.

See addrs.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'test.dat'
fn = 'test2.dat'
fn = 'addrs.dat'

# Check if sequences contain abba pattern
def has_abba(seqs):
    return any(s[i] == s[i-3] and s[i-1] == s[i-2] and s[i] != s[i-1]
            for s in seqs for i in range(3, len(s)))

# Scan list of sequences and extract aba patterns
def find_aba(seqs):
    return [ s[i-2:i+1] for s in seqs
            for i in range(2, len(s))
            if s[i] == s[i-2] and s[i-1] != s[i] ]

# Given an aba list, scan the sequences for the corresponding bab list
def has_bab(seqs, aba_list):
    bab_list = [ f"{b}{a}{b}" for a, b, c in aba_list ]
    return any(a in s for s in seqs for a in bab_list)

# Read lines and split into lists of outside-brackets and inside-brackets
# Format: abcdefgh[abc]defgjij[askdfj]zxcvnak
with open(fn, 'r') as file:
    addr_list = [ (a[0::2], a[1::2]) for a in (re.split('\[|\]', line.strip()) for line in file) ]

count = sum(has_abba(a[0]) and not has_abba(a[1]) for a in addr_list)
print(f"Part 1 is {count}")

count = sum(has_bab(a[1], find_aba(a[0])) for a in addr_list)
print(f"Part 2 is {count}")
