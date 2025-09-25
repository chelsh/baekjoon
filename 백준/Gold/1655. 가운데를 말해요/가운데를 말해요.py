import sys
import heapq

N = int(sys.stdin.readline())

low = []
high = []

for _ in range(N):
	num = int(sys.stdin.readline())

	if len(low) == 0 or num <= -low[0]:
		heapq.heappush(low, -num)
	else:
		heapq.heappush(high, num)

	if len(low) < len(high):
		root = heapq.heappop(high)
		heapq.heappush(low, -root)
	elif len(low) > len(high) + 1:
		root = heapq.heappop(low)
		heapq.heappush(high, -root)

	print(-low[0])
