f = open("input.txt")
grid = [list(x.strip()) for x in f]

ROWS, COLS = len(grid), len(grid[0])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

areas = []

visit = set()
def area(r, c, ele):
	area, perimeter = 0, 0
	def dfs(r, c, ele):
		nonlocal area, perimeter
		area += 1
		visit.add((r, c))
		num_adj = 0
		for dr, dc in dirs:
			nr, nc = r + dr, c + dc
			if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == ele:
				num_adj += 1
				if (nr, nc) not in visit:
					dfs(nr, nc, ele)
		perimeter += 4 - num_adj

	dfs(r, c, ele)
	return (area, perimeter)

s = 0
for r in range(ROWS):
	for c in range(COLS):
		if (r, c) not in visit:
			a, p = area(r, c, grid[r][c])
			s += a * p
			areas.append((grid[r][c], a, p))

print("Part 1:", s)

# PART 2
visit_global = set()
def area(r, c, ele):
	global visit_global
	area = 0
	visit = set()

	def dfs(r, c, ele):
		nonlocal area
		area += 1
		visit.add((r, c))
		for dr, dc in dirs:
			nr, nc = r + dr, c + dc
			if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == ele:
				if (nr, nc) not in visit:
					dfs(nr, nc, ele)

	dfs(r, c, ele)
	visit_global = visit_global.union(visit)

	s = sides(r, c, ele, visit)

	return area, s

def sides(r, c, ele, graph):
	visit = set()
	sides = {(0, 1): 0, (1, 0): 0, (0, -1): 0, (-1, 0): 0}

	def dfs(r, c, ele, dir):
		visit.add((r, c))
		for dr, dc in dirs:
			nr, nc = r + dr, c + dc
			if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visit and grid[nr][nc] == ele:
				nnr, nnc = nr + dir[0], nc + dir[1]
				if not (nnr in range(ROWS) and nnc in range(COLS) and grid[nnr][nnc] == ele):
					dfs(nr, nc, ele, dir)

	for side in sides:
		s = 0
		for r in range(ROWS):
			for c in range(COLS):
				if (r, c) in graph and (r, c) not in visit and grid[r][c] == ele:
					nr, nc = r + side[0], c + side[1]
					if not (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == ele):
						dfs(r, c, grid[r][c], side)
						s += 1

		sides[side] += s
		visit.clear()

	return sum(sides.values())

s = 0
for r in range(ROWS):
	for c in range(COLS):
		if (r, c) not in visit_global:
			a, side = area(r, c, grid[r][c])
			s += a * side

print("Part 2:", s)