import sys
from collections import deque

T = int(sys.stdin.readline())
results = []

for _ in range(T):
	N, M = [int(n) for n in sys.stdin.readline().split()]
	priorities = [int(n) for n in sys.stdin.readline().split()]

	docs = deque()
	for i in range(N):
		docs.append((i,priorities[i]))

	printed = 0

	while True:
		cur = docs.popleft()
		for original_order, priority in docs:
			if priority > cur[1]:
				docs.append(cur)
				break
		else:
			printed += 1
			if cur[0] == M:
				results.append(str(printed))
				break

print("\n".join(results))