import sys
from collections import deque
sys.setrecursionlimit(300000)

N, R, Q = [int(n) for n in sys.stdin.readline().split()]
edges_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
queries = [int(sys.stdin.readline()) for _ in range(Q)]

edges = [[] for _ in range(N+1)]
for u, v in edges_list:
	edges[u].append(v)
	edges[v].append(u)

sizes = [1 for _ in range(N+1)]
stack = deque()

def dfs(cur):
	global stack
	global sizes
	stack.append(cur)
	if len(edges[cur]) > 0:
		for child in edges[cur]:
			edges[child].remove(cur)
			dfs(child)
			sizes[cur] += sizes[child]
	stack.pop()

dfs(R)
result = []
for q in queries:
	result.append(str(sizes[q]))
print("\n".join(result))