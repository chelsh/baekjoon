def lotto(L):
    k = L[0]
    S = L[1:]
    a, b, c, d, e, f = [0, 1, 2, 3, 4, 5]
    idxList = [a, b, c, d, e, f]

    cnt = k - 6
    targetIdx = 5

    while a != k - 5:
        for i in idxList:
            print(S[i], end=" ")

        if cnt != 0:
            idxList[targetIdx] += 1
            cnt -= 1
        else:
            targetIdx -= 1
            idxList[targetIdx] += 1
            cnt = 1

        print(idxList)
        print(targetIdx)
        print(cnt)
        print()



while True:
    T = [int(n) for n in input().split()]
    if T == [0]:
        break
    else:
        lotto(T)
