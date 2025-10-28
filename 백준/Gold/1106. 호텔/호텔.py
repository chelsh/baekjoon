import sys
import math

C, N = [int(n) for n in sys.stdin.readline().split()]
c = [0]
p = [0]
for _ in range(N):
	cost, people = [int(n) for n in sys.stdin.readline().split()]
	c.append(cost)
	p.append(people)

dp = [[0] * (N+1)]
i = 1
flag = True
while flag:
	dp.append([0] * (N+1))
	for j in range(1, N+1):
		if i < c[j]:
			dp[i][j] = dp[i][j-1]
		else:
			dp[i][j] = max(dp[i][j-1], dp[i-c[j]][j] + p[j])

	for people in dp[i]:
		if people >= C:
			flag = False
			print(i)
			break
	i += 1
