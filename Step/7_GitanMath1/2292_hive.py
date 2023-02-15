N = int(input())
L = [1]
i = 0
while L[-1] < N:
    add = 6 * (i + 1)
    start = L[-1]
    L.append(start + add)
    i += 1
print(i+1)  #or print(len(L))