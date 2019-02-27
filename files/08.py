import re

class Register:
    def __init__(self, title, value=0):
        self.title = title
        self.value = value

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.title} is {self.value}>'


class Instruction:
    def __init__(self, target, op, value, cond):
        self.target = target
        self.op = op
        self.value = value
        self.cond = cond

    def __repr__(self):
        return f'<I {self.target} {self.op} {self.value} if {self.cond}>'


def parse_input(filepath):

    with open(filepath) as file:
        lines = [ln.split() for ln in file.readlines()]

    registers = {}
    instructions = []
    for ln in lines:
        targ_reg = ln[0]
        cond_reg = ln[4]
        for reg in [targ_reg, cond_reg]:
            registers[reg] = Register(reg)
        op = "+" if ln[1] == 'inc' else "-"
        value = ln[2]
        cond = f"registers['{cond_reg}'].value {ln[5]} {ln[6]}"
        instructions.append(Instruction(targ_reg, op, value, cond))

    return registers, instructions


def do_instructions(registers, instructions):
    for i in instructions:
        if eval(i.cond) is True:
            r_value = str(registers[i.target].value)
            registers[i.target].value = eval(f'{r_value} {i.op} {i.value}')

    return registers


def find_max_value(registers):
    return max([r.value for r in registers.values()])



################################################################################
if __name__ == '__main__':
    filepath = "08.txt"
    registers, instructions = parse_input(filepath)
    registers = do_instructions(registers, instructions)
    pt1 = find_max_value(registers)

    print(f"Part 1: {pt1}")
