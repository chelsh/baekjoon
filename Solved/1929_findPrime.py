import sys
import math

M, N = [int(n) for n in sys.stdin.readline().split()]

for n in range(M, N + 1):
    if n == 1:
        pass
    elif n == 2 or n == 3:
        print(n)
    else:
        for i in range(2, math.ceil(n ** (1/2) + 1)):
            if n % i == 0:
                break
        else:
            print(n)