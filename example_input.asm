;loop ASM. count down from 10
LOD 10 ;load the number 10
STO 200 ; store it at 200
:START LODI 200 ; load the value stored at 200
SUB 1 ; subtract 1 from it
STO 200
OUT ; print it out
JNZ START
HLT
