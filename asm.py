import sys


OPCODES = {
	'LOD': "001",
	'STO': "002",
	'ADD': "003", 
	'SUB': "004",
	'JMP': "005",
	'HLT': "006",
	'OUT': "007"
}

def parse_instruction(ins, index):
	state = 0 # state 0 is instruction, state 1 is arguments
	last_state = -1
	buf = ""

	struct = ""
	args = []
	EOS = lambda x,y: y == x[-1] # determine if we've reached the end of a string

	if ins:
		for char in ins:
			if (char ==" " or EOS(ins, char)) and state == 0: 
				if state == 0:
					state = 1
					struct = buf
					buf = ""
			elif (char =="," or EOS(ins, char)) and state == 1:
				args.append(buf)
				buf = ""
			elif state ==2:
				continue
			elif state == 2 and EOS(ins,char):
				break
			elif char == ";":
				if buf:
					args.append(buf)
				state = 2 # comments state
			else:
				buf+= char
		return struct, args

def get_raw(ins, args):
	mach_code = str(OPCODES[ins.strip()])
	for arg in args:
		mach_code+= (" "+arg)
	mach_code+="\n" 
	return mach_code

output = open('output.asm', "w+")

for index, instruction in enumerate(open(sys.argv[1], "r")):
 	ins, args = parse_instruction(instruction, index)
 	if ins:
		output.write(get_raw(ins, args))

output.close()
print "successful assembly"
