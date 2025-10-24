import sys
from collections import deque

N = int(sys.stdin.readline())
goal = [int(sys.stdin.readline()) for _ in range(N)]
nums = sorted(goal)
stack = deque()

cur = 0
operations = []

for i in range(N):
	stack.append(nums[i])
	operations.append("+")
	while len(stack) > 0:
		if stack[-1] == goal[cur]:
			stack.pop()
			cur += 1
			operations.append("-")
		else:
			break

if len(stack) > 0:
	print("NO")
else:
	print("\n".join(operations))