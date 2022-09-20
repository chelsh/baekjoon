N, M = [int(n) for n in input().split()]
cards = [int(n) for n in input().split()]

def comb(arr, n):
    L = []
    if n > len(arr):
        return L

    elif n == 1:
        for i in arr:
            L.append([i])

    for i in range(len(arr) - n + 1):
        for j in comb(arr[i + 1:], n - 1):
            L.append([arr[i]] + j)
    return L

print(comb(cards, 3))


# blackjack = []
# for i in comb(cards, 3):
#     if i < M:
#         blackjack.append(i)
# print(max(blackjack))