import sys

N = int(sys.stdin.readline())
L = [[int(n) for n in sys.stdin.readline().split()] for _ in range(N)]

dp = L

for i in range(len(L) - 1):
    for j in range(len(L[i]) + 1):
        if j == 0:
            dp[i + 1][j] += dp[i][0]
        elif j == len(L[i]):
            dp[i + 1][j] += dp[i][-1]
        else:
            dp[i + 1][j] += max(dp[i][j - 1], dp[i][j])

result = max(dp[-1])
print(result)