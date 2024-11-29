# PRIME
The **P**ython-supported **R**untime for **I**ntelligent **M**achine **E**xecution
## Explanation
The PRIME Machine is a Python - interpreted software that gives you an easy way to simulate a real computer.
It has all, from the registers to a specific binary format, including a memory sistem with special memory-management related functions,
and various graphic interface commands, to enhance the user point of view of your program.
Furthermore, as a quickly - development project, an OS and an assembler will be soon added.

## Basic Guide
As the 1<sup>st</sup> edition (`computer1.py`) has a deprecated syntax, it won't be explained as much as the 2<sup>nd</sup>.

__*The following characteristics are mainly for the 2<sup>nd</sup> version, and could not be implemented in the first*__

The special syntax of this machine is quite basic and straightforward.
It has 16 bit (2B) opcodes, and the distinctive trait from other machnes is that only the first 8 bit of the opcode are occupied by the instruction.
The other 8 bit of the opcode are two parameters (each of 4 bit), often referring at registers.
That leads us to a 1B instruction.  
The machine has a set of 16 registers, together with the accumulator register, and space for 16 subroutines (functions).  
In general:
 - opcode: 16 bit
   - 8 bit -> instruction
   - 4 bit x 2 -> parameters
 - 16-bit registers
 - 16 registers
 - 16 subroutine functions
