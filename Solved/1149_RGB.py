N = int(input())
L = []

for _ in range(N):
    L.append([int(i) for i in input().split()])

dp = [L[0]]

for i in range(1, N):
    dp.append([L[i][0] + min(dp[i - 1][1], dp[i - 1][2]),
     L[i][1] + min(dp[i - 1][0], dp[i - 1][2]),
     L[i][2] + min(dp[i - 1][0], dp[i - 1][1])])

print(min(dp[-1]))




#Wrong Answer
# N = int(input())
# L = []

# for _ in range(N):
#     L.append([int(i) for i in input().split()])

# dpR = [L[0][0]];dpG = [L[0][1]];dpB = [L[0][2]]  #각각 R, G, B로 시작


# def exceptPrev(p):
#     if p == 0:
#         a, b = 1, 2
#     elif p == 1:
#         a, b = 0, 2
#     elif p == 2:
#         a, b = 0, 1
#     return a, b

# def RGB(dp, prev):
#     if N == 2:
#         a, b = exceptPrev(prev)
#         return L[0][prev] + min(L[1][a], L[1][b])

#     else:
#         for i in range(1, N - 1):
#             a, b = exceptPrev(prev)
            
#             route1 = L[i][a] + min(L[i+1][prev], L[i+1][b])
#             route2 = L[i][b] + min(L[i+1][prev], L[i+1][a])

#             if route1 == route2:
#                 if L[i][a] <= L[i][b]:
#                     prev = a
#                 else:
#                     prev = b
#             else:
#                 if route1 < route2:
#                     prev = a
#                 else:
#                     prev = b

#             dp.append(L[i][prev])

#         a, b = exceptPrev(prev)
#         dp.append(min(L[N - 1][a], L[N - 1][b]))

#         return sum(dp)


# print(min(RGB(dpR, 0), RGB(dpG, 1), RGB(dpB, 2)))
