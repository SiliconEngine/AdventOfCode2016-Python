# Advent of Code 2016 solutions written in Python.
## Author: Tim Behrendsen

Link: https://adventofcode.com/2016/

Advent of Code is a series of puzzles over 25 days, each with a part 1 and
part 2. The difficulty roughly rises each day, with the later puzzles often
requiring some tricky algorithms to solve.

For these solutions, the various days are in separate directories, with a
separate file for each part. Day 25, as traditional, is only a single part.

### Advent of Code 2016, Day 1, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/1

Given a list of right and left turns and distances, follow the path and
compute the taxi distance. Part 2 traces the entire path and figures out where
visits the same coordinates twice.

### Advent of Code 2016, Day 2, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/2

The data is a path around a keypad, which we need to follow to produce an
entry code. Part 1 is a simple number grid. Part 2 is a more complex grid.

### Advent of Code 2016, Day 3, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/3

Given a list of triangles, calculate how many are valid by ensuring that the sum
of the shortest sides exceeds the long side. Part 1 takes the list as-is, while Part 2
has each set of three rows in a single column is a triangle.

### Advent of Code 2016, Day 4, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/4

The input data is a list of "rooms" identified by a hash. Some of the rooms are
invalid, so step 1 counts the valid ones using the supplied method. Part 2 decodes
the rooms and finds the "North Pole Object Storage" room, which required scanning
the output and finding the correct phrase.

### Advent of Code 2016, Day 5, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/5

Given an md5-based password encoding scheme, decode a password based on a "door ID".
Part 1 and part 2 use a bit different algorithms

### Advent of Code 2016, Day 6, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/6

Given a list of words, for Part 1, construct a word where each letter is the most frequent
letter in the column of the list. Part 2 is the least frequent letter in the column.

### Advent of Code 2016, Day 7, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/7

We're given a list of security patterns, each with letters outside of brackets, and
letters inside of brackets.

For Part 1, identify letters that are of pattern of [letter1][letter2][letter2][letter1]
that are contained outside of brackets, but don't have that pattern inside the brackets.

For Part 2, identify all [letter1][letter2][letter1] patterns outside brackets that are
also have [letter2][letter1][letter2] inside the brackets.

### Advent of Code 2016, Day 8, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/8

We're given instructions to draw pixels on a display, then rotate rows or columns
by various amounts. Part 1 counts the number of final pixels, and Part 2 displays
the drawn letters.

### Advent of Code 2016, Day 9, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/9

Input data is a sequence of characters with repeat counts in parenethesis. Part 1
calculates the total length of the final sequence, accounting for the repeating, but not
repeating the repeat counts. Part 2 allows repeat count sequences to themselves be
repeated, which is solved with recursion.

Part 1 example: A(2x2)BCD(2x2)EFG = 11
Part 2 example: (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN = 445

### Advent of Code 2016, Day 10, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/10

The input is a list of bot rules, where they trade numbered "chips", and are eventually
put into a numbered output bin. Part 1: Figure out which bot compares value-61 chips with
value 17 chips. Part 2 is figuring out what chip numbers end up in output bins 0, 1, and 2.

### Advent of Code 2016, Day 11, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/11

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

### Advent of Code 2016, Day 12, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/12

Simulate a simple CPU and execute the given program. Part 1 display contents of
register 'a' after running. Part 2 does the same thing after initializing
register 'c' to 1.

### Advent of Code 2016, Day 13, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/13

Calculate the shortest distance to a node in a maze. The maze is specified
by a given formula that determines if a node is a wall or open. Part 2
gives the number of nodes within 50 moves of the origin.

### Advent of Code 2016, Day 14, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/14

Scan a series of MD5 hashes based on an salt + index, and find ones with the
following properties:

1) Must have three hex digits in a row
2) For these, one of the hashes in the next 1000 must have five of that hex digit in
a row.

For Part 1, it finds the index of the 64th hash with that property. For Part 2, the
hash generation is changed such that each has is itself hashed 2016 times, and
other the algorithm is the same.

### Advent of Code 2016, Day 15, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/15

Given a set of rotating discs with different numbers of slots, we want to
find how much time to wait before dropping a "capsule" so that it falls
through all the slots. Each disc is one second apart and it takes one second
to reach the first disc.

Part 2 adds an additional disc.

### Advent of Code 2016, Day 16, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/16

Apply a "dragon algorithm" to a string of binary digits, then apply a reducing algorithm.
Part 2 increases the size.

### Advent of Code 2016, Day 17, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/17

Navigate a maze and get the shortest (part 1) and longest (part 2) paths to the
end point. The wrinkle is that whether doors in a room are open or not is based
on the MD5 hash of a "passcode" and the prior directions of the path to the room.

### Advent of Code 2016, Day 18, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/18

Implements a 1D cellular automata and counts the number of spaces. Part 2 just
increases the number of cycles.

### Advent of Code 2016, Day 19, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/19

A group of elves sits in a circle, each with a Christmas present. On each elf turn,
they take the presents from another elf, and the elf without presents is removed
from the circle. Find which elf ends up with all the presents.

In Part 1, the current elf takes the presents from the elf on their immediate left
(facing the circle). In Part 2, the current elf takes the presents from the elf across
the circle.

This puzzle was all about efficient data structures. Part 1 uses "deque" from the
Python standard library. Part 2 uses a single-linked ring buffer. Most of the run
time is spent initializing the data structures.

There's likely also a formula that can just calculate the final result, but I didn't
go looking for that.

### Advent of Code 2016, Day 20, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/20

Given a set of ranges of invalid integer IP addresses, for Part 1, figure out
the lowest valid address. For Part 2, figure out the total number of valid
addresses.

### Advent of Code 2016, Day 21, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/21

We're given a list of string manipulation instructions. For Part 1, we apply the
various manipulations to a "password" and produce the encoded result. For Part 2,
we have to reverse the moves and turn an encoded result back into a password.

Reversing the instruction we're mostly straightforward, with the exception of one
that had complicated rules ("rotate based on position of letter x"). That one
required building a table of reverse rotations and adding a special instruction
for it.

### Advent of Code 2016, Day 22, Part 1 and (not) Part 2

Link: https://adventofcode.com/2016/day/22

We're given a list of filesystems accessible through a network. We can move all files
from one "adjacent" filesystem to another. Part 1 figures out how many filesystems
can move their files to a different files with sufficient capacity.

It turns out that Part 2 can't be solved in a general way, and the intent was to
manually calculate the answer because of the example data was very specific. There
are ways to solve it limiting oneself to those assumptions.

### Advent of Code 2016, Day 23, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/23

Uses the simple CPU from Day 12, with an extra instruction that "toggles" an
instruction type elsewhere in the code. Part 1 runs with register 'a' set to 7,
which quickly produces a result. Part 2 sets 'a' to 12, which takes a long time
to run.

By analyzing the flow of instructions, the inner loop was identified, and I added
an optimization that does a multiply instead of repeated addition

### Advent of Code 2016, Day 24, Part 1 and Part 2

Link: https://adventofcode.com/2016/day/24

We're given a maze of "HVAC ducts", with certain points marked with a series of
numbers. In Part 1, our task is to start at '0' and navigate the maze visiting
all the numbers, finding the length of the shortest path. In Part 2, we have to
navigate the same way, but end up at the origin.

Uses Breadth-First-Search where each node is coordinates + bitmap of visited numbers.
Part 1 and Part 2 could be combined by keeping an intermediate result of reaching
the final number, and the continuing until reaching the origin.

### Advent of Code 2016, Day 25

Link: https://adventofcode.com/2016/day/25

Uses the CPU simulator from Day 12. We need to set register 'a' to the right
value that produces an alternating sequence of 0 and 1. We now have an extra
instruction 'out' for outputting the number. The exec() routine was changed
to yield based on that output instruction.

