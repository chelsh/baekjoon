def prime(m, n):
    L = []
    for i in range(m, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            if i != 1:
                L.append(i)
    if len(L) == 0:
        return -1
    return str(sum(L)) + "\n" + str(min(L))

M = int(input())
N = int(input())
print(prime(M, N))