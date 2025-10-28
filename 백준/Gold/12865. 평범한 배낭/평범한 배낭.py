import sys

N, K = [int(n) for n in sys.stdin.readline().split()]
W = [0]
V = [0]
for _ in range(N):
    w, v = [int(n) for n in sys.stdin.readline().split()]
    W.append(w)
    V.append(v)

dp = [[0] * (N + 1) for _ in range(K+1)] 

for i in range(1, K+1):
    for j in range(1, N+1):
        if i < W[j]:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-W[j]][j-1] + V[j])

print(max(dp[K]))