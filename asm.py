import sys
from parse_machine import ParsingMachine


parser = ParsingMachine()

output = open('output.asm', "w+")
code = map(str.strip, open(sys.argv[1], "r").readlines())
final_code = parser.parse(code)


for line in final_code:
	for sym in line:
		if sym:
			output.write(str(int(sym)).zfill(3))
	output.write("\n")
output.close()
print "successful assembly"
