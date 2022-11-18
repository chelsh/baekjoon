# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# def comb(n, r):
#     return factorial(n) // (factorial(r) * factorial(n - r))

# def tile(n):
#     result = 0
#     two = n // 2

#     for i in range(two + 1):
#         result += comb(n, i)
#         i -= 1
    
#     return L


# print(tile(int(input())) % 10007)





#DP
n = int(input())

L = [1, 2]

for i in range(2, n):
    L.append(L[i - 2] + L[i - 1])

print(L[n - 1] % 10007)