T = int(input())

for i in range(T):
    k = int(input());n = int(input())   
    L = [[j for j in range(1, n + 1)]]
    for l in range(k):
        L.append([sum(L[-1][:m + 1])for m in range(n)])
    print(L[-1][-1])