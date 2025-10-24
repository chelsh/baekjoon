import sys

R, C = [int(n) for n in sys.stdin.readline().split()]
grid = [list(sys.stdin.readline().strip()) for _ in range(R)]

dirs = [(-1,1),(0,1),(1,1)]

cnt = 0

def dfs(y, x):
	global cnt
	grid[y][x] = "x"

	if x == C-1:
		cnt += 1
		return True

	for dy, dx in dirs:
		ny, nx = y+dy, x+dx
		if 0 <= ny < R and 0 <= nx < C:
			if grid[ny][nx] == ".":
				next_result = dfs(ny, nx)
				if not next_result:
					continue
				else:
					return True
	else:
		return False

for i in range(R):
	dfs(i,0)

print(cnt)