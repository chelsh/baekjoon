import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
	N, K = [int(n) for n in sys.stdin.readline().split()]
	delays = [0] + [int(n) for n in sys.stdin.readline().split()]

	orders = []
	for _ in range(K):
		orders.append([int(n) for n in sys.stdin.readline().split()])

	W = int(sys.stdin.readline())

	graph = [[] for _ in range(N+1)]
	indegree = [0]*(N+1)
	dp = [0]*(N+1)

	for i in range(K):
		a, b = orders[i]
		graph[a].append(b)
		indegree[b] += 1

	q = deque()

	for i in range(1, N+1):
		if indegree[i] == 0:
			q.append(i)
			dp[i] = delays[i]

	while q:
		u = q.popleft()
		for v in graph[u]:
			dp[v] = max(dp[v], delays[v]+dp[u])
			indegree[v] -= 1
			if indegree[v] == 0:
				q.append(v)

	print(dp[W])
