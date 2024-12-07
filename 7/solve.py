import itertools
import tqdm

f = open("input.txt")
items = []
for line in f:
	val, ops = line.split(":")
	val = int(val)
	ops = [int(x) for x in ops.strip().split()]
	items.append([val, ops])

ADD, MUL, CONCAT = 0, 1, 2

ans = 0

for item in tqdm.tqdm(items):
	val = item[0]
	nos = item[1]

	for x in itertools.product(range(2), repeat=len(nos)-1):
		s = nos[0]
		for i in range(1, len(nos)):
			if x[i-1] == ADD:
				s += nos[i]
			else:
				s *= nos[i]
		if s == val:
			ans += val
			break

print("Part 1:", ans)

# PART 2
ans = 0

for item in tqdm.tqdm(items):
	val = item[0]
	nos = item[1]

	for x in itertools.product(range(3), repeat=len(nos)-1):
		s = nos[0]
		for i in range(1, len(nos)):
			if x[i-1] == ADD:
				s += nos[i]
			elif x[i-1] == MUL:
				s *= nos[i]
			else:
				s = int(str(s) + str(nos[i]))
		if s == val:
			ans += val
			break

print("Part 2:", ans)