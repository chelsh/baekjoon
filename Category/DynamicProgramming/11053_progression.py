N = int(input())

A = [int(n) for n in input().split()]

dp = [[A[i]] for i in range(N)]

for i in range(N):
    for j in range(i - 1 , -1, -1):
        if A[j] < dp[i][0]:
            dp[i] = [A[j]] + dp[i]
    for j in range(i + 1, N):
        if A[j] > dp[i][-1]:
            dp[i].append(A[j])

for i in range(N):
    dp[i] = len(dp[i])

print(max(dp))