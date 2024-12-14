import re, functools, subprocess, time
import tqdm

f = open("input.txt")
robots = []

for line in f:
	m = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
	pos = (int(m.group(1)), int(m.group(2)))
	velocity = (int(m.group(3)), int(m.group(4)))
	robots.append((pos, velocity))

LENGTH, WIDTH = 103, 101

robots_ini = robots.copy()

def move():
	for i in range(len(robots)):
		pos, vel = robots[i]
		new_pos = ((pos[0] + vel[0]) % WIDTH, (pos[1] + vel[1]) % LENGTH)
		robots[i] = (new_pos, vel)

for _ in range(100):
	move()

num_in_quadrants = [0, 0, 0, 0]
for robot in robots:
	pos = robot[0]
	if pos[0] in range(WIDTH // 2) and pos[1] in range(LENGTH // 2):
		num_in_quadrants[0] += 1 	# 1st quadrant	
	elif pos[0] in range(WIDTH // 2 + 1, WIDTH) and pos[1] in range(LENGTH // 2):
		num_in_quadrants[1] += 1 	# 2nd quadrant	
	elif pos[0] in range(WIDTH // 2 + 1, WIDTH) and pos[1] in range(LENGTH // 2 + 1, LENGTH):
		num_in_quadrants[2] += 1 	# 3rd quadrant	
	elif pos[0] in range(WIDTH // 2) and pos[1] in range(LENGTH // 2 + 1, LENGTH):
		num_in_quadrants[3] += 1 	# 4th quadrant	

part_1 = functools.reduce(lambda x, y: x * y, num_in_quadrants)
print("Part 1:", part_1)
f.close()

# PART 2:
robots = robots_ini

def check_if_in_line(x, y, positions):
	DIRS = [(0, 1), (0, -1)]	# UP or DOWN
	LINE_LENGTH = 10

	visit = set()
	def dfs(x, y, line_length):
		if line_length == 0:
			return True
		visit.add((x, y))
		for dx, dy in DIRS:
			nx, ny = x + dx, y + dy
			if nx in range(WIDTH) and ny in range(LENGTH) and (nx, ny) not in visit and (nx, ny) in positions:
				if dfs(nx, ny, line_length - 1):
					return True
		return False

	return dfs(x, y, LINE_LENGTH)

def draw_robots():
	grid = [['.' for _ in range(WIDTH)] for _ in range(LENGTH)]
	for robot in robots:
		pos = robot[0]
		grid[pos[1]][pos[0]] = '*'
	for r in range(LENGTH):
		print(*grid[r])

time = 0
tries = 0
pbar = tqdm.tqdm(total=10000)
while True:
	move()
	time += 1
	pbar.update(1)
	positions = [robot[0] for robot in robots]
	for robot in robots:
		pos = robot[0]
		if check_if_in_line(pos[0], pos[1], positions):
			draw_robots()
			tries += 1
			break
	if tries == 1:
		break
pbar.close()

print("Part 2:", time)