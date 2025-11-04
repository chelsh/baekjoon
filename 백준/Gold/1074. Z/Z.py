import sys

N, y, x = [int(n) for n in sys.stdin.readline().split()]

s, e = 1, 2**(2*N)
ax, bx = 0, 2**N - 1
ay, by = 0, 2**N - 1

while s != e:
	half_side = (by-ay) // 2 + 1
	quarter = (e-s+1) // 4
	if ay <= y < ay+half_side:
		by -= half_side
		if ax <= x < ax+half_side:
			bx -= half_side
			e -= 3 * quarter
		else:
			ax += half_side
			s += quarter
			e -= 2 * quarter
	else:
		ay += half_side
		if ax <= x < ax+half_side:
			bx -= half_side
			s += 2 * quarter
			e -= quarter
		else:
			ax += half_side
			s += 3 * quarter

print(s-1)