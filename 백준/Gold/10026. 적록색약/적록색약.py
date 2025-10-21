import sys
from collections import deque

N = int(sys.stdin.readline())
grid = []
for _ in range(N):
	grid.append(list(sys.stdin.readline().strip()))

visited = [[False] * N for _ in range(N)]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

red = []
green = []
blue = []

for r in range(N):
	for c in range(N):
		if visited[r][c] == False:
			visited[r][c] = True

			color = grid[r][c]

			q = deque()
			q.append((r,c))
			group = [(r,c)]

			while q:
				y, x = q.popleft()

				for dy, dx in dirs:
					ny, nx = y+dy, x+dx
					if 0 <= ny < N and 0 <= nx < N:
						if visited[ny][nx] == False and grid[ny][nx] == color:
							visited[ny][nx] = True
							q.append((ny,nx))
							group.append((ny,nx))

			if grid[y][x] == "R":
				red.append(group)
			elif grid[y][x] == "G":
				green.append(group)
			elif grid[y][x] == "B":
				blue.append(group)

rg = [[False] * N for _ in range(N)]
rg_visited = [[False] * N for _ in range(N)]
for r_group in red:
	for y, x in r_group:
		rg[y][x] = True
for g_group in green:
	for y, x in g_group:
		rg[y][x] = True

red_green = []

for r in range(N):
	for c in range(N):
		if rg[r][c] == True and rg_visited[r][c] == False:
			rg_visited[r][c] = True

			q = deque()
			q.append((r,c))

			group = [(r,c)]

			while q:
				y, x = q.popleft()
				for dy, dx in dirs:
					ny, nx = y+dy, x+dx
					if 0 <= ny < N and 0 <= nx < N:
						if rg_visited[ny][nx] == False and rg[ny][nx] == True:
							rg_visited[ny][nx] = True
							q.append((ny,nx))
							group.append((ny,nx))
			red_green.append(group)

not_color_blind = len(red) + len(green) + len(blue)
color_blind = len(red_green) + len(blue)

print(not_color_blind, color_blind)
