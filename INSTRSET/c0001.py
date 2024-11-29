from numpy import sin, cos, tan, hypot, radians, power, log, exp

class c0001():
    def __init__(self, mainclass, operation, par1, par2, reg1, reg2, instrn):
        try:
            match operation:
                case '0000': #SUM
                    a=int(mainclass.tempreg,2)
                    if par1=="0000":
                        b=0
                        c=int(reg2,2)
                    else:
                        b=par1+par2
                        b=int(b,2)
                        c=0
                    a+=b
                    a+=c
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '0001': #SUB
                    a=int(mainclass.tempreg,2)
                    if par1=="0000":
                        b=0
                        c=int(reg2,2)
                    else:
                        b=par1+par2
                        b=int(b,2)
                        c=0
                    a-=b
                    a-=c
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '0010': #MUL
                    a=int(mainclass.tempreg,2)
                    if par1=="0000":
                        b=0
                        c=int(reg2,2)
                    else:
                        b=par1+par2
                        b=int(b,2)
                        c=0
                    a*=b
                    a*=c
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '0011': #DEV
                    a=int(mainclass.tempreg,2)
                    if par1=="0000":
                        b=0
                        c=int(reg2,2)
                    else:
                        b=par1+par2
                        b=int(b,2)
                        c=0
                    a/=b
                    a/=c
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '0100': #MOD
                    a=int(mainclass.tempreg,2)
                    if par1=="0000":
                        b=0
                        c=int(reg2,2)
                    else:
                        b=par1+par2
                        b=int(b,2)
                        c=0
                    a%=b
                    a%=c
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '0101': #IND
                    a=int(mainclass.tempreg,2)
                    if par1=="0000":
                        b=0
                        c=int(reg2,2)
                    else:
                        b=par1+par2
                        b=int(b,2)
                        c=0
                    a//=b
                    a//=c
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '0110': #POW
                    a=int(mainclass.tempreg,2)
                    if par1=="0000":
                        c=int(reg2,2)
                        a=power(a,c)
                    else:
                        b=par1+par2
                        b=int(b,2)
                        a=power(a,b)
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '0111': #ROT
                    a=int(mainclass.tempreg,2)
                    if par1=="0000":
                        c=int(reg2,2)
                        c=1/c
                        a=power(a,c)
                    else:
                        b=par1+par2
                        b=int(b,2)
                        b=1/b
                        a=power(a,b)
                    a=int(a)
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '1000': #LGN
                    a=int(mainclass.tempreg,2)
                    a=log(a)
                    a=int(a)
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '1001': #EXP
                    a=int(mainclass.tempreg,2)
                    a=exp(a)
                    a=int(a)
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '1010': #SIN
                    a=int(mainclass.tempreg,2)
                    b=int(reg1,2)
                    b=radians(b)
                    a=sin(a)
                    a*=b
                    a=int(a)
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '1011': #COS
                    a=int(mainclass.tempreg,2)
                    b=int(reg1,2)
                    b=radians(b)
                    a=cos(a)
                    a*=b
                    a=int(a)
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '1100': #TAN
                    a=int(mainclass.tempreg,2)
                    b=int(reg1,2)
                    b=radians(b)
                    a=tan(a)
                    a*=b
                    a=int(a)
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '1101': #HYP
                    a=int(mainclass.tempreg,2)
                    b=int(reg1,2)
                    a=hypot(a,b)
                    a=int(a)
                    a=bin(a)
                    a=a[2:]
                    if len(a)>16:
                        x=len(a)-16
                        a=a[x:]
                    else:
                        x=16-len(a)
                        a='0'*x+a
                    mainclass.tempreg=a
                case '1110':
                    print(int(reg1,2))
                case '1111': #NOP
                    pass
        except IndexError:
            print("Index error: Make sure register indices are within bounds.")
        except ValueError:
            print("Value error: Check register contents and instruction format.")