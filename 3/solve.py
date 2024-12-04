import re

f = open("input.txt")
s = 0

do = True

for line in f:
	matches = re.findall(r"mul\((\d?\d?\d?),(\d?\d?\d?)\)|(don't\(\))|(do\(\))", line)
	# print(matches)
	for match in matches:
		if match[2] == "don't()":
			do = False
		elif match[3] == "do()":
			do = True
		else:
			if do:
				s += int(match[0]) * int(match[1])

print(s)