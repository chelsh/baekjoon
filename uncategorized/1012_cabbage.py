import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = [int(n) for n in sys.stdin.readline().split()]
    L = []

    for _ in range(K):
        L.append([int(n) for n in sys.stdin.readline().split()])
    
    for 