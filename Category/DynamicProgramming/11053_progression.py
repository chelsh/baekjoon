N = int(input())

L = [int(n) for n in input().split()]

dp = [1] * N

for i in range(1, N):
    m = 0
    for j in range(i):
        if L[i] > L[j]:
            if dp[j] > m:
                m = dp[j]
    dp[i] += m

print(max(dp))



# N = int(input())

# A = [int(n) for n in input().split()]
# dp = [1] * N
# dpp = [[] for i in range(N)]
# print(dpp)

# for i in range(N - 1):
#     m = A[i]
#     n = A[i]
#     dpp[i].append(n)
#     for j in range(i + 1, N):
#         if A[j] > m:
#             m = A[j]
#             dp[i] += 1

#     for k in range(i, -1, -1):
#         if A[k] < n:
#             n = A[k]
#             dp[i] += 1
#             dpp[i].append(n)

# print(max(dp))
# print(dpp)
