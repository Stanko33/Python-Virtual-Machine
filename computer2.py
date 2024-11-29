import random, re
from INSTRSET.c0000 import *
from INSTRSET.c0001 import *
from INSTRSET.c0010 import *
from INSTRSET.c0011 import *
from INSTRSET.c0100 import *
from INSTRSET.c0101 import *
from INSTRSET.c0110 import *
from INSTRSET.c0111 import *
from INSTRSET.c1000 import *
from INSTRSET.c1001 import *
from INSTRSET.c1010 import *
from INSTRSET.c1011 import *
from INSTRSET.c1100 import *
from INSTRSET.c1101 import *
from INSTRSET.c1110 import *
from INSTRSET.c1111 import *


class Main():
    instr = 0

    registers = [
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000',
        '0000000000000000'
    ]
    tempreg = "0000000000000000"
    dot = ''
    subroutines = [
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
    ]
    program = ''
    programcommands = []

    @staticmethod
    def bootstrap():
        for i in range(random.randint(2, 5)):
            print('bootstrapping...')
        os_path = os.path.join(os.getcwd(), "OS")
        with open(os_path, "r") as prog:
            program=prog.read()
            print(program)
            program=program.replace('\n', '')
            program=program.replace(' ', '')
            program=re.sub(r'/.*?/', '', program)
            Main.uncomprog(program)

    @staticmethod
    def decinstr(instruction, linenum):
        instruction = str(instruction)
        type = instruction[0:4]
        operation = instruction[4:8]
        par1 = instruction[8:12]
        par2 = instruction[12:16]
        instruction_number = linenum
        reg1 = Main.registers[int(par1, 2)]
        reg2 = Main.registers[int(par2, 2)]
        match type:
            case '0000':
                c0000(Main, operation, par1, par2, reg1, reg2, instruction_number)
            case '0001':
                c0001(Main, operation, par1, par2, reg1, reg2, instruction_number)
            case '0010':
                c0010(Main, operation, par1, par2, reg1, reg2, instruction_number)
            case _:
                print("Feature still not implemented!")

    @staticmethod
    def uncomprog(program):
        Main.programcommands = [program[i:i+16] for i in range(0, len(program), 16)]
        while Main.instr < len(Main.programcommands):
            Main.decinstr(Main.programcommands[Main.instr], Main.instr)
            Main.instr += 1


# Move this code OUTSIDE the Main class
progshell = input('CHOOSE BETWEEN SHELL INPUT OR BOOTSTRAPPING OS (S/O): ').strip().upper()
if progshell == 'O':
    Main.bootstrap()
else:
    while True:
        shell = input('Shell command: ')
        print('Executing:', shell)
        Main.uncomprog(shell)
