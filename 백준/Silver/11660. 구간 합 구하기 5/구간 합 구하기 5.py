import sys

N, M = [int(n) for n in sys.stdin.readline().split()]
grid = [[0]*(N+1)]
for _ in range(N):
	grid.append([0, *list(map(int, sys.stdin.readline().split()))])

for i in range(1, N+1):
	for j in range(1, N+1):
		grid[i][j] += grid[i][j-1] + grid[i-1][j] - grid[i-1][j-1]

result = []
for _ in range(M):
	x1, y1, x2, y2 = [int(n) for n in sys.stdin.readline().split()]
	result.append(str(grid[x2][y2] - grid[x2][y1-1] - grid[x1-1][y2] + grid[x1-1][y1-1]))
print("\n".join(result))