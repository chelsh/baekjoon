import sys

results = []

while True:
	triangle = [int(n) for n in sys.stdin.readline().split()]
	if triangle[0] == triangle[1] == triangle[2] == 0:
		break
	else:
		triangle.sort()
		if triangle[2]**2 == triangle[0]**2 + triangle[1]**2:
			results.append("right")
		else:
			results.append("wrong")

print("\n".join(results))