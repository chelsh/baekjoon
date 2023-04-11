N = int(input())
def hansu(N):
    nums = list(range(1, N+1))
    hansu = 0
    for n in nums:
        L = [int(i) for i in list(str(n))]
        d_list = [L[i] - L[i + 1] for i in range(len(L) - 1)]
        d_set = set(d_list)
        if len(d_set) == 0 or len(d_set) == 1:
            hansu += 1
    return hansu
print(hansu(N))

# if len(d_set) == 0 or 1:   <- if문 정상작동X