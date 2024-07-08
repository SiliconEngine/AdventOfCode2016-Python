#!/usr/bin/python
"""Advent of Code 2016, Day 25

https://adventofcode.com/2016/day/25

Uses the CPU simulator from Day 12. We need to set register 'a' to the right
value that produces an alternating sequence of 0 and 1. We now have an extra
instruction 'out' for outputting the number. The exec() routine was changed
to yield based on that output instruction.

See program.dat for full data.

Author: Tim Behrendsen
"""

fn = 'program.dat'
from itertools import count

class CPU:
    def __init__(self, program=None):
        if program != None:
            self.load(program)
        self.reset()

    def reset(self):
        self.regs = { 'a': 0, 'b': 0, 'c': 0, 'd': 0 }

    def get_p(self, p):
        return int(p) if p.isnumeric() else self.regs[p]

    def load(self, program):
        self.program = program

    def exec(self):
        pc = 0
        while pc < len(self.program):
            instr = self.program[pc]
            if instr[0] == 'cpy':
                self.regs[instr[2]] = self.get_p(instr[1])
            elif instr[0] == 'inc':
                self.regs[instr[1]] += 1
            elif instr[0] == 'dec':
                self.regs[instr[1]] -= 1
            elif instr[0] == 'jnz':
                if self.get_p(instr[1]) != 0:
                    pc += int(instr[2])-1
            elif instr[0] == 'out':
                yield self.get_p(instr[1])

            pc += 1

# Try numbers until the output sequence tests as alternating 0/1
cpu = CPU([ line.strip().split(' ') for line in open(fn, 'r') ])
for a in count(0):
    cpu.reset()
    cpu.regs['a'] = a
    exec = cpu.exec()
    last = next(exec)
    for _ in range(20):
        n, expect = next(exec), 1-last
        if n != expect:
            break
        last = n
    if n == expect:
        break

print(f"Answer is {a}")
