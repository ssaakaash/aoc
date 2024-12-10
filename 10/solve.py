f = open("input.txt")
grid = [[int(y) for y in x.strip()] for x in f]

ROWS, COLS = len(grid), len(grid[0])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

level_0 = []
for r in range(ROWS):
	for c in range(COLS):
		if grid[r][c] == 0:
			level_0.append((r, c))

# PART 1
def find_score(r, c):
	visit = set()
	def dfs(r, c, next_num):
		if grid[r][c] == 9:
			visit.add((r, c))
		for dr, dc in dirs:
			nr, nc = r + dr, c + dc
			if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == next_num:
				dfs(nr, nc, next_num + 1)
	dfs(r, c, 1)
	return len(visit)

s = 0
for r, c in level_0:
	s += find_score(r, c)

print("Part 1:", s)

# PART 2
def find_score(r, c):
	rating = 0
	def dfs(r, c, next_num):
		nonlocal rating
		if grid[r][c] == 9:
			rating += 1
		for dr, dc in dirs:
			nr, nc = r + dr, c + dc
			if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == next_num:
				dfs(nr, nc, next_num + 1)
	dfs(r, c, 1)
	return rating

s = 0
for r, c in level_0:
	s += find_score(r, c)

print("Part 2:", s)