f = open("input.txt")
grid = [list(x.strip()) for x in f]

ROWS, COLS = len(grid), len(grid[0])

# PART 1
def traverse(r, c, dir):
	nr, nc = r + dir[0], c + dir[1]
	if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 'A':
		nr, nc = nr + dir[0], nc + dir[1]
		if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 'S':
			return True
	return False

def search(r, c):
	count = 0
	dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
	for dr, dc in dirs:
		nr, nc = r + dr, c + dc
		if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 'M':
			if traverse(nr, nc, (dr, dc)):
				count += 1
	return count

found = 0
for r in range(ROWS):
	for c in range(COLS):
		if grid[r][c] == 'X':
			found += search(r, c)

print("Part 1:", found)

# PART 2
def check_xmas(r, c, dir):
	nr, nc = r + dir[0], c + dir[1]
	xmas = {'M', 'S'}
	if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] in xmas:
		xmas.remove(grid[nr][nc])
		nr, nc = r - dir[0], c - dir[1]
		if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] in xmas:
			xmas.remove(grid[nr][nc])
	return len(xmas) == 0

def isxmas(r, c):
	return check_xmas(r, c, (1, 1)) and check_xmas(r, c, (1, -1))

found = 0
for r in range(ROWS):
	for c in range(COLS):
		if grid[r][c] == 'A' and isxmas(r, c):
			found += 1

print("Part 2:", found)