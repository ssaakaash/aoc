f = open("input.txt")
nos = [int(x) for x in f.read().split()]

cache = {}
def blink(num, times):
	if (num, times) in cache:
		return cache[(num, times)]

	if times == 0:
		return 1

	if num == 0:
		count = blink(1, times - 1)
		cache[(num, times)] = count
		return count

	if len(str(num)) % 2 == 0:
		first = int(str(num)[:len(str(num)) // 2])
		second = int(str(num)[len(str(num)) // 2:])

		count_first = blink(first, times - 1)
		count_second = blink(second, times - 1)

		cache[(num, times)] = count_first + count_second
		return count_first + count_second

	count = blink(num * 2024, times - 1)
	cache[(num, times)] = count
	return count

# PART 1
total = 0
for num in nos:
	total += blink(num, 25)

print("Part 1:", total)

# PART 2
total = 0
for num in nos:
	total += blink(num, 75)

print("Part 2:", total)