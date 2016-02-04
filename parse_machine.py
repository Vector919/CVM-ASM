
OPCODES = {
	'LOD': "001",
	'STO': "002",
	'ADD': "003", 
	'SUB': "004",
	'JMP': "005",
	'HLT': "006",
	'OUT': "007",
	'JMPZ': "008",
	'LODI': "009",
	'JNZ': "010"
}

STATE_INSTRUCTION = 0
STATE_ARGUMENTS = 1
STATE_COMMENTS = 2
STATE_SYMBOL = 3
STATE_DEF_SYMBOL = 4



COMMENT_CHAR = ";"
DEF_SYMBOL_CHAR = ":"

class ParsingMachine(object):

	def __init__(self):
		self.symbols = {}
		self.symbol_count = 0

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
						if buf not in self.symbols:
							args.append(buf)
						else:
							args.append(self.symbols[buf])
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
						state = STATE_ARGUMENTS

					elif state == STATE_ARGUMENTS:
						if buf not in self.symbols:
							args.append(buf)
						else:
							args.append(self.symbols[buf])

					elif state == STATE_DEF_SYMBOL:
						self.symbols[buf] = self.symbol_count
						state = STATE_INSTRUCTION
					else:
						pass

					self.symbol_count +=1
					buf = ""
					continue

				if current_input == COMMENT_CHAR:
					state = STATE_COMMENTS

				if current_input == DEF_SYMBOL_CHAR:
					state = STATE_DEF_SYMBOL
					continue

				buf+=current_input
			if instruction:
				output.append([OPCODES[instruction]]+args)
		return output
