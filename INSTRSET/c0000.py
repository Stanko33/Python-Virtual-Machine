import os

helpmessage="""This is a help message for the computer:
The first half of a bite is the class indicator: it indicates which category of commands are you using.
The second half indicates which command of that category are you using.
The second byte indicates two parameters for the command, each made of 4 bits."""

class c0000():
    def __init__(self, mainclass, operation, par1, par2, reg1, reg2, instrn):
        try:
            match operation:
                case '0000': #EXE
                    dir=reg1[2:4]
                    dir=int(dir,2)
                    dir=hex(dir)
                    dir=dir.upper()
                    file=reg1[4:6]
                    file=int(file,2)
                    file=hex(file)
                    file=file.upper()
                    path="MEMORY/"+dir+"/"+file
                    with open(path, "r") as prog:
                        program=prog.read()
                        print(program)
                        program=program.replace('\n', '')
                        mainclass.uncomprog(program)
                case '0001': #HLT
                    exit()
                case '0010': #LOD0
                    mainclass.tempreg=par1+par2+mainclass.tempreg[8:]
                case '0011': #LOD1
                    mainclass.tempreg=mainclass.tempreg[:8]+par1+par2
                case '0100': #LOD
                    mainclass.tempreg=reg1
                case '0101': #STO
                    mainclass.registers[int(par1,2)]=mainclass.tempreg
                case '0110': #JMP
                    line=par1+par2
                    line=int(line,2)-1
                    mainclass.instr=line
                case '0111': #CLS
                    print("\033c")
                case '1000': #DEF
                    nosub=None
                    for subroutine in mainclass.subroutines:
                        if subroutine!="0":
                            continue
                        else:
                            nosub=subroutine
                            break
                    if nosub==None:
                        print("No space for other subroutines!")
                        exit()
                    lineno=instrn
                    while True:
                        instruction = mainclass.programcommands[lineno]
                        if instruction[:8]=='00001001':
                            break
                        mainclass.subroutines[nosub]=mainclass.subroutines[nosub]+instruction
                case '1001': #END
                    pass
                case '1010': #CAL
                    subroutine=mainclass.subroutines[int(par1,2)]
                    mainclass.uncomprog(subroutine)
                case '1011': #HLP
                    print(helpmessage)
                case '1100': #RDM
                    dir=int(par1,2)
                    dir=hex(dir)
                    dir=dir[2:]
                    dir=dir.upper()
                    file=int(par1,2)
                    file=hex(dir)
                    file=dir[2:]
                    file=file.upper()
                    path=f"MEMORY/{dir}/{file}"
                    if os.path.exists(path):
                        with open(path, 'r') as f:
                            data = f.read().strip()
                            if set(data) <= {"0", "1"} and len(data) == 16:  # Validate binary data
                                mainclass.registers[int(par1, 2)] = data
                                print(f"Read data from {dir}/{file}: {data}")
                            else:
                                print(f"Invalid data in {dir}/{file}. Must be 16 bits of 0s and 1s.")
                    else:
                        print(f"Memory location {dir}/{file} does not exist.")
                case '1101': #WRM
                    dir=int(par1,2)
                    dir=hex(dir)
                    dir=dir[2:]
                    dir=dir.upper()
                    file=int(par1,2)
                    file=hex(dir)
                    file=dir[2:]
                    file=file.upper()
                    data = reg1[:16]
                    if len(data) < 16:
                        data = '0'*(16-len(data))+data
                    if set(data) <= {"0", "1"}:
                        path = f"MEMORY/{dir}/{file}"
                        if os.path.exists(path):
                            with open(path, 'a') as f:
                                f.write(data)
                                print(f"Written data to {dir}/{file}: {data}")
                        else:
                            print(f"Memory location {dir}/{file} does not exist.")
                    else:
                        print(f"Invalid register data: {data}. Must contain only 0s and 1s.")
                case '1110': #CLM
                    dir=int(par1,2)
                    dir=hex(dir)
                    dir=dir[2:]
                    dir=dir.upper()
                    file=int(par1,2)
                    file=hex(dir)
                    file=dir[2:]
                    file=file.upper()
                    path = f"MEMORY/{dir}/{file}"
                    if os.path.exists(path):
                        with open(path, 'w') as f:
                            f.write('')
                            print(f"Cleared memory location {dir}/{file}.")
                    else:
                        print(f"Memory location {dir}/{file} does not exist.")
                case '1111': #PRS
                    textreg1=[int(mainclass.registers[int(reg1[i:i+4],2)], 2) for i in range(0,15,4)]
                    textreg2=[int(mainclass.registers[int(reg2[i:i+4],2)], 2) for i in range(0,15,4)]
                    text1,text2='', ''
                    text1=text1+''.join(chr((textreg1[i])) for i in range(0, 4))
                    text2=text2+ ''.join(chr((textreg2[i])) for i in range(0, 4))
                    text=text1+text2
                    print(text, end="")
        except IndexError:
            print("Index error: Make sure register indices are within bounds.")
        except ValueError:
            print("Value error: Check register contents and instruction format.")