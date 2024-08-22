def combination(n, r):
    result = 1
    if r <= n-r:
        for i in range(n, n-r, -1):
            result *= i
        for i in range(1, r+1):
            result //= i
    else:
        s = n-r
        for i in range(n, n-s, -1):
            result *= i
        for i in range(1, s+1):
            result //= i
    print(result)

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = [int(n) for n in sys.stdin.readline().split()]
    combination(M, N)