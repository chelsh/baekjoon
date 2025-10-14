import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    grid = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    visited = [[False] * M for _ in range(N)]

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    worms = 0

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1 and not visited[r][c]:
                worms += 1
                q = deque()
                q.append((r, c))
                visited[r][c] = True

                while q:
                    y, x = q.popleft()
                    for dy, dx in dirs:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M:
                            if grid[ny][nx] == 1 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                q.append((ny, nx))

    print(worms)