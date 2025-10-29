import sys

N = int(sys.stdin.readline())
house = [[0, 0, 0]]
for _ in range(N):
	house.append([int(n) for n in sys.stdin.readline().split()])

INF = 1001

dp_r = [[0, 0, 0], [house[1][0], INF, INF]]
dp_g = [[0, 0, 0], [INF, house[1][1], INF]]
dp_b = [[0, 0, 0], [INF, INF, house[1][2]]]

for i in range(2, N+1):
	R = min(dp_r[i-1][1], dp_r[i-1][2]) + house[i][0]
	G = min(dp_r[i-1][0], dp_r[i-1][2]) + house[i][1]
	B = min(dp_r[i-1][0], dp_r[i-1][1]) + house[i][2]
	dp_r.append([R,G,B])

for i in range(2, N+1):
	R = min(dp_g[i-1][1], dp_g[i-1][2]) + house[i][0]
	G = min(dp_g[i-1][0], dp_g[i-1][2]) + house[i][1]
	B = min(dp_g[i-1][0], dp_g[i-1][1]) + house[i][2]
	dp_g.append([R,G,B])

for i in range(2, N+1):
	R = min(dp_b[i-1][1], dp_b[i-1][2]) + house[i][0]
	G = min(dp_b[i-1][0], dp_b[i-1][2]) + house[i][1]
	B = min(dp_b[i-1][0], dp_b[i-1][1]) + house[i][2]
	dp_b.append([R,G,B])

print(min(dp_r[N][1], dp_r[N][2], dp_g[N][0], dp_g[N][2], dp_b[N][0], dp_b[N][1]))
