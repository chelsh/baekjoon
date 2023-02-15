import sys

N, K = [int(n) for n in sys.stdin.readline().split()]

L = []
for _ in range(N):
    L.append(int(sys.stdin.readline()))

cnt = 0

while K != 0:
    for i in range(N - 1):
        if L[i] <= K and K < L[i + 1]:
            coin = L[i]
            break
    if L[-1] <= K:
        coin = L[-1]
        break
    
    while coin <= K:
        K -= coin
        cnt += 1

print(cnt)