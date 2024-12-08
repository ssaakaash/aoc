import tqdm

f = open("input.txt")

graph = [list(line.strip()) for line in f]
ROWS, COLS = len(graph), len(graph[0])

UP, LEFT, DOWN, RIGHT = (-1, 0), (0, -1), (1, 0), (0, 1)
dirs = [UP, RIGHT, DOWN, LEFT]

for r in range(ROWS):
	for c in range(COLS):
		if graph[r][c] in ('^', '<', '>', 'v'):
			start = (r, c)
			if graph[r][c] == '^':
				startdir = 0
			elif graph[r][c] == '<':
				startdir = 3
			elif graph[r][c] == 'v':
				startdir = 2
			else:
				startdir = 1
			break

r, c = start
dir = startdir
graph[r][c] = 'X'

# PART 1
count = 1
while True:
	nr, nc = r + dirs[dir][0], c + dirs[dir][1]
	if nr not in range(ROWS) or nc not in range(COLS):
		graph[r][c] = 'X'
		count += 1
		break
	if graph[nr][nc] == '#':
		dir = (dir + 1) % 4
		continue
	if graph[r][c] != 'X':
		graph[r][c] = 'X'
		count += 1
	r, c = nr, nc

print("Part 1:", count)

# PART 2
f.seek(0)
graph = [list(line.strip()) for line in f]

def is_loop(block):
	dir = startdir
	r, c = start

	visit = set()
	while True:
		nr, nc = r + dirs[dir][0], c + dirs[dir][1]
		if nr not in range(ROWS) or nc not in range(COLS):
			return False
		if graph[nr][nc] == '#' or (nr, nc) == block:
			visit.add((r, c, dir))
			dir = (dir + 1) % 4
			continue
		if (r, c, dir) in visit:
			return True
		visit.add((r, c, dir))
		r, c = nr, nc

count = 0
for r in tqdm.tqdm(range(ROWS)):
	for c in range(COLS):
		if is_loop((r, c)):
			count += 1

print("Part 2:", count)
