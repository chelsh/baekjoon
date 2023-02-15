import sys

N, M = [int(n) for n in sys.stdin.readline().split()]
L = [int(n) for n in sys.stdin.readline().split()]

cnt = 0

for i in range(len(L)):
    while L[i] != 0:
        if L[i] == 1:
            N -= 1
            for j in range(i, len(L)):
                L[j] -= 1
        elif L[i] <= (N + 1) // 2:
            cnt += 1
            for j in range(i, len(L)):
                if L[j] == 1:
                    L[j] = N
                else:
                    L[j] -= 1
        else:
            cnt += 1
            for j in range(i, len(L)):
                if L[j] == N:
                    L[j] = 1
                else:
                    L[j] += 1

print(cnt)