from collections import deque

f = open("input.txt")

graph = {}
for line in f:
	if line == "\n":
		pages = f.readlines()
		break
	a, b = [int(x) for x in line.strip().split('|')]
	if a not in graph:
		graph[a] = {b}
	else:
		graph[a].add(b)

pages = [[int(x) for x in s.strip().split(',')] for s in pages]

# PART 1
def is_topological_sort(l):
	visited = set()
	sort = deque()
	def dfs(x):
		if x in visited:
			return
		visited.add(x)
		if x in graph:
			for v in graph[x]:
				if v in l:
					dfs(v)
		sort.appendleft(x)

	for v in l:
		dfs(v)

	return list(sort) == l

s = 0
for page in pages:
	if is_topological_sort(page):
		s += page[len(page) // 2]

print("Part 1:", s)

# PART 2
def topological_sort(l):
	visited = set()
	sort = deque()
	def dfs(x):
		if x in visited:
			return
		visited.add(x)
		if x in graph:
			for v in graph[x]:
				if v in l:
					dfs(v)
		sort.appendleft(x)

	for v in l:
		dfs(v)

	return list(sort)

s = 0
for page in pages:
	if not is_topological_sort(page):
		l = topological_sort(page)
		s += l[len(l) // 2]

print("Part 2:", s)


