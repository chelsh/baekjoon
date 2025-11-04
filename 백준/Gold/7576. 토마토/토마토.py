import sys
from collections import deque

M, N = [int(n) for n in sys.stdin.readline().split()]
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dirs = ((-1,0),(0,1),(1,0),(0,-1))
cnt = 0
days = 0

q = deque()

for y in range(N):
	for x in range(M):
		if grid[y][x] == 1:
			q.append((y,x))
			cnt += 1
		elif grid[y][x] == -1:
			cnt += 1

while q:
	cur = len(q)
	for _ in range(cur):
		y, x = q.popleft()
		for dy, dx in dirs:
			ny, nx = y+dy, x+dx
			if 0 <= ny < N and 0 <= nx < M:
				if grid[ny][nx] == 0:
					q.append((ny,nx))
					grid[ny][nx] = 1
					cnt += 1
	days += 1

if cnt != M*N:
	print(-1)
else:
	print(days-1)