import sys

N = int(sys.stdin.readline())
solutions = [int(n) for n in sys.stdin.readline().split()]

best = 2_000_000_001
best_pair = None

l = 0
r = N-1

while l < r:
	s = solutions[l] + solutions[r]
	if best > abs(s):
		best = abs(s)
		best_pair = (solutions[l], solutions[r])
	if s < 0:
		l += 1
	elif s > 0:
		r -= 1
	else:
		best_pair = (solutions[l], solutions[r])
		break

print(best_pair[0], best_pair[1])
