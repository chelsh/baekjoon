import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
s = str(N)
length = len(s)
numList = [int(s[i]) for i in range(length)]

L = [n for n in range(10)]
ect = [int(n) for n in sys.stdin.readline().split()]
for n in ect:
    L.remove(n)

#case1: +- only
d = abs(N - 100)

#case2: use number button
numBtn = length
if len(L) == 1:
    for i in range(length):
        numBtn += L[0] * (10 ** i)

else:
    for i in range(length):
        if numList[i] in L:
            numList[i] = [numList[i]]
        else:
            l = L
            l.append(n).sort()
            idx = l.index(n)
            if i != length - 1:
                






    #         if len(L) == 2:
    #             numList[i] = L
    #         else:
    #             l = L
    #             l.append(n).sort()
    #             idx = l.index(n)
    #             if idx == len(l) - 1:
    #                 numList[i] = [l[-2]]
    #             elif idx == 0:
    #                 numList[i] = [l[1]]
    #             else:
    #                 numList[i] = [l[idx - 1], l[idx + 1]]
                
    # for i in range(length):
        






print(min(d, numBtn))
