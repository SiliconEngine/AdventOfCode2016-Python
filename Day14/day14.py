#!/usr/bin/python
"""Advent of Code 2016, Day 14, Part 1 and Part 2

https://adventofcode.com/2016/day/14

Scan a series of MD5 hashes based on an salt + index, and find ones with the
following properties:

1) Must have three hex digits in a row
2) For these, one of the hashes in the next 1000 must have five of that hex digit in
a row.

For Part 1, it finds the index of the 64th hash with that property. For Part 2, the
hash generation is changed such that each has is itself hashed 2016 times, and
other the algorithm is the same.

Author: Tim Behrendsen
"""

from hashlib import md5
from collections import deque
import re

salt = 'yjdafjpo'

# Generate key for an index
def key(idx, step):
    k = md5((salt + str(idx)).encode('utf-8')).hexdigest()
    if step == 2:
        for i in range(2016):
            k = md5(k.encode('utf-8')).hexdigest()
    return k

# Iterator to produce next item that has at least one pattern match
def next_item(step):
    idx = 0
    while True:
        k = key(idx, step)
        m3 = re.findall(r'(.)\1\1', k)
        m3 = None if len(m3) == 0 else m3[0]
        m5 = re.findall(r'(.)\1\1\1\1', k)
        if m3 != None or len(m5):
            yield (idx, m3, m5)     # (int, char, list)
        idx += 1

def run(step):
    get = next_item(step)       # Iterator for next item set
    queue, count = deque(), 0
    while count < 64:
        work3 = queue.popleft() if queue else next(get)
        if work3[1] != None:
            # Make sure we have enough items for index + 1000
            while len(queue) == 0 or queue[-1][0] < (work3[0] + 1000):
                queue.append(next(get))

            for work5 in queue:
                if work5[0] - work3[0] > 1000:
                    break
                if work3[1] in work5[2]:
                    count += 1
                    break

    return work3[0]

print(f"Step 1 is {run(1)}")
print(f"Step 2 is {run(2)}")
