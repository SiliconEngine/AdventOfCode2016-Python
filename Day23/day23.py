#!/usr/bin/python
"""Advent of Code 2016, Day 23, Part 1 and Part 2

https://adventofcode.com/2016/day/23

Uses the simple CPU from Day 12, with an extra instruction that "toggles" an
instruction type elsewhere in the code. Part 1 runs with register 'a' set to 7,
which quickly produces a result. Part 2 sets 'a' to 12, which takes a long time
to run.

By analyzing the flow of instructions, the inner loop was identified, and I added
an optimization that does a multiply instead of repeated addition

See program.dat for full data.

Author: Tim Behrendsen
"""

import re, time

fn = 'program.dat'

class CPU:
    def __init__(self, program=None):
        self.regs = { k: 0 for k in 'abcd' }
        if program != None:
            self.load(program)

    def get_p(self, p):
        return int(p) if re.match(r'-{0,1}\d+', p) else self.regs[p]

    def load(self, program):
        self.program = [ i.copy() for i in program ]

    def exec(self):
        tgl_map = { 'inc': 'dec', 'dec': 'inc', 'tgl': 'inc', 'jnz': 'cpy', 'cpy': 'jnz' }

        pc = 0
        while pc < len(self.program):
            # Optimization for inner loop
            if pc == 5:
                self.regs['a'] += self.regs['c'] * self.regs['d']
                self.regs['c'] = 0
                self.regs['d'] = 0
                pc = 10

            instr = self.program[pc]
            if instr[0] == 'cpy':
                if instr[2].isnumeric():
                    pc += 1             # Invalid instruction after a toggle, ignore
                    continue
                self.regs[instr[2]] = self.get_p(instr[1])
            elif instr[0] == 'inc':
                self.regs[instr[1]] += 1
            elif instr[0] == 'dec':
                self.regs[instr[1]] -= 1
            elif instr[0] == 'jnz':
                if self.get_p(instr[1]) != 0:
                    pc += self.get_p(instr[2])-1
            elif instr[0] == 'tgl':
                chg_pc = pc + self.get_p(instr[1])
                if chg_pc < len(self.program):
                    self.program[chg_pc][0] = tgl_map[self.program[chg_pc][0]]

            pc += 1


with open(fn, 'r') as file:
    program = [ line.strip().split(' ') for line in file ]

cpu = CPU(program)
cpu.regs['a'] = 7
cpu.exec()
print(f"Part 1 is {cpu.regs['a']}")

cpu = CPU(program)
cpu.regs['a'] = 12
cpu.exec()
print(f"Part 2 is {cpu.regs['a']}")
