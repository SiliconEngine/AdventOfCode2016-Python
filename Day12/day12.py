#!/usr/bin/python
"""Advent of Code 2016, Day 12, Part 1 and Part 2

https://adventofcode.com/2016/day/12

Simulate a simple CPU and execute the given program. Part 1 display contents of
register 'a' after running. Part 2 does the same thing after initializing
register 'c' to 1.

See program.dat for full data.

Author: Tim Behrendsen
"""

fn = 'program.dat'

class CPU:
    def __init__(self, program=None):
        self.regs = { 'a': 0, 'b': 0, 'c': 0, 'd': 0 }
        if program != None:
            self.load(program)

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

            pc += 1


with open(fn, 'r') as file:
    program = [ line.strip().split(' ') for line in file ]

cpu = CPU(program)
cpu.exec()
print(f"Part 1 is {cpu.regs['a']}")

cpu = CPU(program)
cpu.regs['c'] = 1
cpu.exec()
print(f"Part 2 is {cpu.regs['a']}")
