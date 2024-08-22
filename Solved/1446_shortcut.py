import sys

N, D = [int(n) for n in sys.stdin.readline().split()]
L = []
for _ in range(N):
    L.append([int(n) for n in sys.stdin.readline().split()])

dis = [i for i in range(D + 1)]

for i in range(D+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i-1] + 1)
    for scut in L:
        s, e, d = scut
        if i == s and e <= D and dis[e] > dis[i] + d:
            dis[e] = dis[i] + d

print(dis[D])
