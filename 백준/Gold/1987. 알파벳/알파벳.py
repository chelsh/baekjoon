import sys
sys.setrecursionlimit(1000000)

R, C = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(R)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cache = {}

def count_tiles(r, c, mask):
    key = (r, c, mask)
    if key in cache:
        return cache[key]

    best = 1
    for dy, dx in dirs:
        ny, nx = r + dy, c + dx
        if 0 <= ny < R and 0 <= nx < C:
            bit = 1 << (ord(grid[ny][nx]) - 65)
            if not (bit & mask):
                best = max(best, 1 + count_tiles(ny, nx, mask | bit))

    cache[key] = best
    return best

start_tile_bit = 1 << (ord(grid[0][0]) - 65)
print(count_tiles(0, 0, start_tile_bit))
