import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = [int(n) for n in sys.stdin.readline().split()]
    d = y - x
    
    s = math.floor(d ** (1 / 2))
    if d == s ** 2:
        print(s*2 - 1)
    elif d <= s ** 2 + s:
        print(s * 2)
    else:
        print((s + 1) * 2 - 1)