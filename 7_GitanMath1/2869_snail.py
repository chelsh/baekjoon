A, B, V = [int(i) for i in input().split()]
for n in range(V):
    V += B * n - A * (n + 1)
    if 