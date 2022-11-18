# #Top-Down
# def add123(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return add123(n - 1) + add123(n - 2) + add123(n - 3)

# for _ in range(int(input())):
#     print(add123(int(input())))



#Bottom-Up 
def add123(n):
    L = [1, 2, 4]
    for i in range(3, n):
        L.append(L[i - 3] + L[i - 2] + L[i - 1])
    return L[n - 1]

for _ in range(int(input())):
    print(add123(int(input())))