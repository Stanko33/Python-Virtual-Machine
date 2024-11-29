from numpy import sin, cos, tan, radians
import random

instr = 0

registers = [
    '00000000',
    '00000000',
    '00000000',
    '00000000',
    '00000000',
    '00000000',
    '00000000',
    '00000000',
    '00000000',
    '00000000'
]
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

def bootstrap():
    for i in range(random.randint(2,5)):print('bootstrapping...')
    with open("MEMORY/OS.py") as file:
        exec(file.read())

def decinstr(instruction, linenum):
    global registers, subroutines, dot, program, instr
    instruction = str(instruction)
    operation = instruction[0:4]
    par1 = instruction[4:8]
    par2 = instruction[8:12]
    par3 = instruction[12:16]
    instruction_number = linenum

    try:
        match operation:
            case '0000':
                registers[int(par3, 2)]=bin(int(int(registers[int(par1, 2)], 2)+int(registers[int(par2, 2)], 2)))[2:]
            case '0001':
                registers[int(par3, 2)]=bin(int(int(registers[int(par1, 2)], 2)-int(registers[int(par2, 2)], 2)))[2:]
            case '0010':
                registers[int(par3, 2)]=bin(int(int(registers[int(par1, 2)], 2)*int(registers[int(par2, 2)], 2)))[2:]
            case '0011':
                registers[int(par3, 2)]=bin(int(int(registers[int(par1, 2)], 2)/int(registers[int(par2, 2)], 2)))[2:]
            case '0100':
                registers[int(par3, 2)]=bin(int(int(registers[int(par1, 2)], 2)**int(registers[int(par2, 2)], 2)))[2:]
            case '0101':
                registers[int(par3, 2)]=bin(int(int(registers[int(par1, 2)], 2)**(1/int(registers[int(par2, 2)], 2))))[2:]
            case '0110':
                registers[int(par3, 2)]=bin(int(sin(radians(int(registers[int(par1, 2)], 2)))*(1/int(registers[int(par2, 2)], 2))))[2:]
            case '0111':
                registers[int(par3, 2)]=bin(int(cos(radians(int(registers[int(par1, 2)], 2)))*(1/int(registers[int(par2, 2)], 2))))[2:]
            case '1000':
                registers[int(par3, 2)]=bin(int(tan(radians(int(registers[int(par1, 2)], 2)))*(1/int(registers[int(par2, 2)], 2))))[2:]
            case '1001':
                loop = []
                if par1 == "0000": repeattimes = int((par2+par3), 2)
                else: repeattimes = int(registers[int(par1, 2)], 2)
                foundloop = 0
                for i in range(instruction_number+1, len(programcommands)):
                    aninstr = programcommands[i]
                    if aninstr[0:4] == "1001":
                        foundloop+=1
                    if aninstr[0:4] == '1011' and foundloop!=0:
                        foundloop-=1
                    elif aninstr[0:4] == '1011':
                        enddo = i
                for i in range(instruction_number+1, instruction_number+enddo):
                    loop.append(programcommands[i])
                for _ in range(repeattimes):
                    for i in range(len(loop)):
                        decinstr(loop[i])
            case '1010':
                #to implement, should be the SUB command
                pass
            case '1011':
                pass #this is the END (END of a function/subroutine) command
            case '1100':
                addlay1 = bin_to_hex(par1)
                addlay2 = bin_to_hex(par2)
                address = f"/MEMORY/{addlay1}/{addlay2}"
                with open(address, 'r') as file:
                    program = file.read().strip()
                    uncomprog(program)
            case '1101':
                print(par1+par2+par3)
                match par1:
                    case '0000':
                        toprint = registers[int(par2, 2)]
                        print(toprint)
    
                    case '0001':
                        toprint = int(registers[int(par2, 2)], 2)
                        print(toprint)
    
                    case '0010':
                        toprint = chr(int(registers[int(par2, 2)], 2))
                        print(toprint)
    
            
            case '1110':
                registers[int(par1, 2)]=par2+par3
            case '1111':
                pass #this should be the LOM (LOad Memory) command
    except IndexError:
        print("Index error: Make sure register indices are within bounds.")
    except ValueError:
        print("Value error: Check register contents and instruction format.")

def uncomprog(program):
    global programcommands, instr
    programcommands = [program[i:i+16] for i in range(0, len(program), 16)]
    if instr!=len(programcommands): decinstr(programcommands[instr], instr)

def bin_to_hex(bin_str):
    decimal_value = int(bin_str, 2)
    return format(decimal_value, 'X')

progshell = input('CHOOSE BETWEEN SHELL INPUT OR BOOTSTRAPPING OS (S/O): ').strip().upper()
if progshell == 'O':
    bootstrap()
else:
    while True:
        shell = input('Shell command: ')
        print('Executing:', shell)
        uncomprog(shell)
