f = open("input.txt")
left = []
right = []

for line in f:
	l, r = [int(x) for x in line.split()]
	left.append(l)
	right.append(r)

left.sort()
right.sort()

# PART 1
s = 0
for i in range(len(left)):
	s += abs(left[i] - right[i])

print("Part 1 difference total:", s)

# PART 2
score = 0
for l in left:
	count = 0
	for r in right:
		if r == l:
			count += 1
	score += l * count

print("Part 2 similarity:", score)