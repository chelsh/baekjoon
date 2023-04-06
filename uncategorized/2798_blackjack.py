import sys

N, M = [int(n) for n in sys.stdin.readline().split()]
L = [int(n) for n in sys.stdin.readline().split()]
L.sort()

result = []

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = L[i] + L[j] + L[k]
            if total <= M:
                result.append(total)
            else:
                break

print(max(result))
