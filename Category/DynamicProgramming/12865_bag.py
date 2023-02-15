N, K = [int(n) for n in input().split()]

W = []
V = []

for _ in range(N):
    item = [int(n) for n in input().split()]
    W.append(item[0])
    V.append(item[1])

dp = [[0 for i in range(K)]]

for i in range(N):
    for j in range(K):
        if W[i] > j + 1:
            dp[i][j + 1] = dp[i][j]
        elif W[i] == j + 1:
            if V[i] > dp[i][j]:
                dp[i][j]
        else:
            pass
    dp.append(dp[i])



for L in dp:
    L = max(L)

print(max(dp))