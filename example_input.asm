;loop ASM
LOD 5 ;load the number 5
STO 200 ; store it at 200
LODI 200 ; load the value stored at 200
SUB 1 ; subtract 1 from it
STO 200
OUT ; print it out
JMPZ 9 
JMP 3
HLT
