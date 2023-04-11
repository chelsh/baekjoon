# #Top-Down -> 시간초과
# def make1(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     elif n == 3:
#         return 1
#     else:
#         L = []
#         if n % 3 == 0:
#             L.append(make1(n / 3))
#         if n % 2 == 0:
#             L.append(make1(n / 2))
#         L.append(make1(n - 1))
#         return int(min(L) + 1)

# print(make1(int(input())))





#Bottom-up
def make1(n):
    L = [None] * (n + 3)
    L[1] = 0;L[2] = 1;L[3] = 1
    for i in range(4, n + 1):
        d = []
        if i % 3 == 0:
            d.append(L[int(i / 3)])
        if i % 2 == 0:
            d.append(L[int(i / 2)])
        d.append(L[i - 1])
        L[i] = int(min(d) + 1)
    return L[n]

print(make1(int(input())))