import sys


def stair(L):
    if len(L) == 1:
        return L[0]
        
    elif len(L) == 2:
        return L[0] + L[1]
    
    else:
        dp = []
        dp.append(L[0])
        dp.append(max(L[0], L[0] + L[1]))
        dp.append(max(L[0] + L[2], L[1] + L[2]))

        for i in range(3, len(L)):
            dp.append(max(dp[i - 2] + L[i], dp[i - 3] + L[i - 1] + L[i]))
    
        return dp[-1]

    

N = int(sys.stdin.readline())
stairs = []
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

print(stair(stairs))







#wrong answer
# def stairs(n):
#     L = []
#     result = 0
#     for i in range(n):
#         L.append(int(input()))
#     i = -1
#     step = 0

#     while i > 1 - n:
#         result += L[i]
#         if step == 1 or L[i - 2] > L[i - 1]:
#             step = 2
#             i -= 2
#         else:
#             step = 1
#             i -= 1

#     if i == -n:
#         result += L[i]
#     else:
#         if step == 1:
#             result += L[i]
#         else:
#             result += L[i] + L[i - 1]

#     return result

# print(stairs(int(input())))