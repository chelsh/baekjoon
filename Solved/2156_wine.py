import sys

n = int(sys.stdin.readline())
L = []
for i in range(n):
    L.append(int(sys.stdin.readline()))

if n == 1:
    print(L[0])
elif n == 2:
    print(L[0] + L[1])
elif n == 3:
    print(sum(L) - min(L))
elif n == 4:
    print(max(L[0] + L[1] + L[3], L[0] + L[2] + L[3], L[1] + L[2]))
else:
    dp = [0] * n

    dp[0] = L[0]
    dp[1] = L[0] + L[1]
    dp[2] = max(L[0], L[1]) + L[2]
    dp[3] = max(L[0] + L[2], L[0] + L[1]) + L[3]

    for i in range(4, n):
        dp[i] = max(dp[i-2] + L[i], dp[i-4] + L[i-1] + L[i], dp[i-3] + L[i-1] + L[i])

    print(max(dp))