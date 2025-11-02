N = int(input())

L = [int(n) for n in input().split()]

dp = [1] * N

for i in range(1, N):
    m = 0
    for j in range(i):
        if L[i] > L[j]:
            if dp[j] > m:
                m = dp[j]
    dp[i] += m

print(max(dp))