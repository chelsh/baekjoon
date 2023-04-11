import sys

N = int(sys.stdin.readline())
L = [int(n) for n in sys.stdin.readline().split()]

sumL = [L[0]]
for i in range(1, N):
    if L[i] < 0:
        sumL.append(L[i])
    else:
        if sumL[-1] < 0:
            sumL.append(L[i])
        else:
            sumL[-1] += L[i]

dp = [0] * len(sumL)
dp[0] = sumL[0]

for i in range(1, len(sumL)):
    dp[i] = max(sumL[i], dp[i-1] + sumL[i])

print(max(dp))