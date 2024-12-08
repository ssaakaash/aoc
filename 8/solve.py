import itertools

f = open("input.txt")

grid = [list(x.strip()) for x in f]
ROWS, COLS = len(grid), len(grid[0])

freqs = {}
for r in range(ROWS):
	for c in range(COLS):
		if grid[r][c] != '.':
			if grid[r][c] not in freqs:
				freqs[grid[r][c]] = [(r, c)]
			else:
				freqs[grid[r][c]].append((r, c))

# PART 1:
antinodes = set()
for freq in freqs:
	for pair in itertools.combinations(freqs[freq], 2):
		(r1, c1), (r2, c2) = pair
		r_dist = r2-r1
		c_dist = c2-c1

		if r1 - r_dist in range(ROWS) and c1 - c_dist in range(COLS):
			antinodes.add((r1 - r_dist, c1 - c_dist))
		if r2 + r_dist in range(ROWS) and c2 + c_dist in range(COLS):
			antinodes.add((r2 + r_dist, c2 + c_dist))

print("Part 1:", len(antinodes))

# PART 2
antinodes = set()
for freq in freqs:
	for pair in itertools.combinations(freqs[freq], 2):
		(r1, c1), (r2, c2) = pair

		r_dist = r2-r1
		c_dist = c2-c1

		while r1 in range(ROWS) and c1 in range(COLS):
			antinodes.add((r1, c1))
			r1, c1 = r1 - r_dist, c1 - c_dist
		while r2 in range(ROWS) and c2 in range(COLS):
			antinodes.add((r2, c2))
			r2, c2 = r2 + r_dist, c2 + c_dist

print("Part 2:", len(antinodes))
		