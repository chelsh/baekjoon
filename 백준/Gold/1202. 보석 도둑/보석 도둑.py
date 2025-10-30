import sys
import heapq

N, K = [int(n) for n in sys.stdin.readline().split()]

jewel = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
heapq.heapify(jewel)
bags = [int(sys.stdin.readline()) for _ in range(K)]
bags.sort()

total = 0
values = []
for i in range(K):
	while len(jewel) > 0:
		m, v = jewel[0]
		if m <= bags[i]:
			mass, value = heapq.heappop(jewel)
			heapq.heappush(values, -value)
		else:
			break
	if len(values) > 0:
		max_value = -heapq.heappop(values)
		total += max_value

print(total)