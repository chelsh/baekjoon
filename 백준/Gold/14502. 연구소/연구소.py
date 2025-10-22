import sys
from collections import deque

N, M = [int(n) for n in sys.stdin.readline().split()]
grid = []
for _ in range(N):
	grid.append([int(n) for n in sys.stdin.readline().split()])

regions = [[] for _ in range(3)] # [0] - empty, [1] - wall, [2] - virus

visited = [[False] * M for _ in range(N)]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

# 0, 1, 2 어디있는지 알아내기(list화)
for r in range(N):
	for c in range(M):
		if not visited[r][c]:
			visited[r][c] = True

			q = deque()
			q.append((r,c))

			region = [(r,c)]
			region_type = grid[r][c]

			while q:
				y, x = q.popleft()
				for dy, dx in dirs:
					ny, nx = y+dy, x+dx
					if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and grid[ny][nx] == region_type:
						q.append((ny, nx))
						visited[ny][nx] = True
						region.append((ny,nx))

			for y, x in region:
				regions[region_type].append((y,x)) 


def infect(y, x, virus_grid):
	for dy, dx in dirs:
		ny, nx = y+dy, x+dx
		if 0 <= ny < N and 0 <= nx < M:
			if virus_grid[ny][nx] == 0:
				virus_grid[ny][nx] = 2
				infect(ny, nx, virus_grid)

max_result = 0
# 0인 곳들 3개씩 1로 만드는거 브루트포스 돌리기 - 돌릴때마다 바이러스 퍼뜨려본다음 안전공간(0) 개수 세기 -> results 리스트에 넣기
for i in range(len(regions[0])):
	for j in range(i+1, len(regions[0])):
		for k in range(j+1, len(regions[0])):

			board = [row[:] for row in grid]
			iy, ix = regions[0][i]
			jy, jx = regions[0][j]
			ky, kx = regions[0][k]

			board[iy][ix], board[jy][jx], board[ky][kx] = [1,1,1]

			board_visited = [[False] * M for _ in range(N)]

			cnt = 0

			for vy, vx in regions[2]:
				infect(vy, vx, board)

			for r in range(N):
				for c in range(M):
					if board[r][c] == 0:
						cnt += 1
						
			if cnt > max_result:
				max_result = cnt

# max(results) 출력
print(max_result)