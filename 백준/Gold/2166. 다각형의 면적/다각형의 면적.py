import sys

N = int(sys.stdin.readline())
polygon = []
for _ in range(N):
	x, y = [int(n) for n in sys.stdin.readline().split()]
	polygon.append((x, y))

result = 0
for i in range(N):
	if i != N-1:
		result += polygon[i][0]*polygon[i+1][1] - polygon[i][1]*polygon[i+1][0]
	else:
		result += polygon[N-1][0]*polygon[0][1] - polygon[N-1][1]*polygon[0][0]

result = abs(result) / 2

print(f"{result:.1f}")