import sys

n = int(sys.stdin.readline())
L = []
for i in range(n):
    L.append(int(sys.stdin.readline()))

if n == 1:
    print(L[0])
elif n == 2:
    print(L[0] + L[1])

dp = [0] * n
dp[0] = L[0]
dp[1] = L[0] + L[1]
dp[2] = max(L[0] + L[2], L[1] + L[2])

ss = [0] * n    # 1 == 연속 
ss[0] = 0
ss[1] = 1
ss[2] = 0 if L[0] + L[2] >= L[1] + L[2] else 1

for i in range(3, n):
    



print(L)
print(dp)
print(max(dp))