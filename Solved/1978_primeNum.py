import sys
import math

N = int(sys.stdin.readline())
L = [int(n) for n in sys.stdin.readline().split()]

cnt = 0
for n in L:
    if n == 1:
        pass
    elif n == 2 or n == 3:
        cnt += 1
    else:
        for i in range(2, math.ceil(n ** (1/2) + 1)):
            if n % i == 0:
                break
        else:
            cnt += 1

print(cnt)