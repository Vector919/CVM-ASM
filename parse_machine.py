
OPCODES = {
	'LOD': "001",
	'STO': "002",
	'ADD': "003", 
	'SUB': "004",
	'JMP': "005",
	'HLT': "006",
	'OUT': "007",
	'JMPZ': "008",
	'LODI': "009"

}

STATE_INSTRUCTION = 0
STATE_ARGUMENTS = 1
STATE_COMMENTS = 2
STATE_SYMBOL = 3



COMMENT_CHAR = ";"

class ParsingMachine(object):

	def __init__(self):
		self.syms = {}

	def parse(self, code):
		output = []
		for line in code:
			state = STATE_INSTRUCTION
			input_stream = list(line)
			instruction = ""
			buf = ""
			args = []
			while True:
				if not input_stream:
					if state == STATE_ARGUMENTS:
						args.append(buf)
						buf = ""
					if state == STATE_INSTRUCTION:
						instruction = buf
						buf = ""
					break

				current_input = input_stream.pop(0)
				if state == STATE_COMMENTS:
					continue
				if current_input == " ":
					if state == STATE_INSTRUCTION:
						instruction = buf
						buf = ""
						state = STATE_ARGUMENTS

					if state == STATE_ARGUMENTS:
						args.append(buf)
						buf = ""

				if current_input == COMMENT_CHAR:
					state = STATE_COMMENTS

				buf+=current_input
			if instruction:
				output.append([OPCODES[instruction]]+args)
		return output
