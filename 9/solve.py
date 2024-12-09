import tqdm

f = open("input.txt")
diskmap = [int(x) for x in f.read()]

def generate(dm):
	m = []
	d_id, j = 0, 0
	while j < len(dm):
		if j % 2 == 0:
			m.extend([d_id] * dm[j])
			d_id += 1
		else:
			m.extend(['.'] * dm[j])
		j += 1
	return m

# PART 1
def compress_blocks(m):
	i, j = 0, len(m) - 1
	while True:
		while m[i] != '.':
			i += 1
		while m[j] == '.':
			j -= 1
		if i >= j:
			break
		m[i], m[j] = m[j], m[i]
		i += 1
		j -= 1

def checksum(m):
	i, s = 0, 0
	while m[i] != '.':
		s += int(m[i]) * i
		i += 1
	return s

m = generate(diskmap)
compress_blocks(m)
print("Part 1:", checksum(m))

# PART 2
def find_space(size, m, pos):
	start, end = 0, 0
	while start < pos and end < pos:
		while m[start] != '.':
			start += 1
			if start >= len(m):
				raise Exception("Start pointer over bounds")

		end = start
		while end < len(m) and m[end] == '.':
			end += 1
			if end >= len(m):
				return (0, 0)

		if start >= pos:
			return (0, 0)

		if end - start >= size:
			return (start, start + size)
		start += 1
		end += 1
	else:
		return (0, 0)

def compress_files(m):
	i, j = len(m) - 2, len(m) - 1
	cur_id = int(m[i+1])
	pbar = tqdm.tqdm(total=cur_id)
	while cur_id >= 0:
		while i >= 0:
			if m[i] != cur_id and m[i+1] == cur_id:
				break
			i -= 1

		while j >= 0:
			if m[j] == cur_id:
				break
			j -= 1

		size = j-i

		u, v = find_space(size, m, i+1)
		if (u, v) != (0, 0):
			m[i+1:j+1], m[u:v] = m[u:v], m[i+1:j+1]

		cur_id -= 1
		pbar.update(1)
	pbar.close()

def checksum(m):
	i, s = 0, 0
	while i < len(m):
		if m[i] == '.':
			i += 1
			continue
		s += int(m[i]) * i
		i += 1
	return s

m = generate(diskmap)
compress_files(m)
print("Part 2:", checksum(m))
