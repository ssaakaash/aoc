f = open("input.txt")

safe = 0
notsafe = 0

def check_safe(levels):
	inc = levels[1] - levels[0] > 0
	for i in range(len(levels) - 1):
		diff = levels[i+1] - levels[i]
		print(levels, i, diff)
		if diff == 0 or abs(diff) > 3:
			return False, i
		if diff > 0 and not inc or diff < 0 and inc:
			return False, i
	return True, 0

for line in f:
	levels = [int(x) for x in line.split()]
	issafe, index = check_safe(levels)
	if not issafe:
		for i in range(len(levels)):
			if check_safe(levels[:i] + levels[i+1:])[0]:
				print("======== SAFE ^ =======")
				safe += 1
				break
		else:
			notsafe += 1
			print("======== NOT SAFE ^ =======")
		# if check_safe(levels[:index] + levels[index+1:])[0]:
		# 	print("======== SAFE ^ =======")
		# 	safe += 1
		# elif check_safe(levels[:index+1] + levels[index+2:])[0]:
		# 	print("======== SAFE ^ =======")
		# 	safe += 1
		# else:
		# 	notsafe += 1
		# 	print("======== NOT SAFE ^ =======")
	else:
		safe += 1
		print("======== SAFE ^ =======")

print(safe, notsafe)