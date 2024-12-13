from collections import namedtuple

f = open("input.txt")
Game = namedtuple('Game', 'a b prize')

lines = f.read().split('\n\n')
games = []
for game in lines:
	words = game.split()
	ax, ay = int(words[2].split('+')[1].strip(',')), int(words[3].split('+')[1])
	bx, by = int(words[6].split('+')[1].strip(',')), int(words[7].split('+')[1])
	px, py = int(words[9].split('=')[1].strip(',')), int(words[10].split('=')[1])
	games.append(Game((ax, ay), (bx, by), (px, py)))

def adj(x):
	return [[x[1][1], -x[0][1]], [-x[1][0], x[0][0]]]

def det(x):
	return x[0][0]*x[1][1] - x[0][1]*x[1][0]

def get_sum():
	s = 0
	for game in games:
		A = [[game.a[0], game.b[0]], [game.a[1], game.b[1]]]
		m = []
		for i in adj(A):
			m.append(i[0] * game.prize[0] + i[1] * game.prize[1])
		d = det(A)
		if d == 0:
			continue
		for i in range(len(m)):
			if m[i] % d == 0:
				m[i] //= d
			else:
				m = [0, 0]
				break
		if m != [0, 0]:
			s += 3*m[0] + m[1]
	return s

print("Part 1:", get_sum())

# Part 2
for i in range(len(games)):
	prize = (games[i].prize[0] + 10000000000000, games[i].prize[1] + 10000000000000)
	games[i] = Game(games[i].a, games[i].b, prize)

print("Part 2", get_sum())
