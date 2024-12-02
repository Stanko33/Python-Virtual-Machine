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
 - 16 subroutine functions with **unlimited space**

## Instruction set (for the 2<sup>nd</sup> model)
__BEWARE:__ *since this project is in developement fase, we suggest you to check frequently this document, to ensure your program is up to date and working*
The instruction is 8-bit large and is divided in two pieces of 4-bit. The first indicates a category of instructions, the second indicates the instruction related to the parent category.  
| Hexadecimal | Binary | Explanation                                |
|:-----------:|:------:|:-------------------------------------------|
|      0      |  0000  | System operations                          |
|      1      |  0001  | Math and trigonometrical functions         |
|      2      |  0010  | GUI instructions                           |
|      3      |  0011  | Memory operations (work in progress)       |
|      4      |  0100  | Decision and iteration structures (w.i.p.) |
|      5      |  0101  | Logic (w.i.p.)                             |
|      6      |  0110  |             |
|      7      |  0111  |             |
|      8      |  1000  |             |
|      9      |  1001  |             |
|      A      |  1010  |             |
|      B      |  1011  |             |
|      C      |  1100  |             |
|      D      |  1101  |             |
|      E      |  1110  |             |
|      F      |  1111  |             |

As you can see, six categories could be enough. We will instead fill (hopefully) every cathegory.  
Let's continue with the real commands:
