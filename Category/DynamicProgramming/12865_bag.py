def comb()

def bag(n, k):
    wvDict = dict(); wvList = []
    for i in range(n):
        w, v = [int(j) for j in input().split()]
        wvDict[w] = v

    return

N, K = [int(i) for i in input().split()]
print(bag(N, K))