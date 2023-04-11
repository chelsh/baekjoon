import sys

N = int(sys.stdin.readline())
L = [int(n) for n in sys.stdin.readline().split()]

sumL = [L[0]]
for i in range(1, N):
    if L[i] < 0:
        sumL.append(L[i])
    else:
        if sumL[-1] < 0:
            sumL.append(L[i])
        else:
            sumL[-1] += L[i]

print(sumL)
if max(sumL) <= 0:
    print(max(sumL))
else:
    dp = [sumL[0] if sumL[0] >= 0 else 0]

    for i in range(1, len(sumL)):
        if sumL[i] >= 0:
            dp.append(sumL[i])
        else:
            if i != len(sumL) - 1:
                if sumL[i] + sumL[i + 1] >= 0:
                    dp.append(dp[-1] + sumL[i] + sumL[i + 1])
                    sumL[i + 1] = dp[-1]
    print(dp)
    print(max(dp))
            





#메모리 초과
# import sys

# N = int(sys.stdin.readline())
# L = [int(n) for n in sys.stdin.readline().split()]

# sumL = [L[0]]
# for i in range(1, N):
#     if L[i] < 0:
#         sumL.append(L[i])
#     else:
#         if sumL[-1] < 0:
#             sumL.append(L[i])
#         else:
#             sumL[-1] += L[i]

# dp = []

# length = len(sumL)
# for i in range(length - 1):
#     dp.append(sumL[i])
#     for j in range(i + 1, length):
#         dp.append(dp[-1] + sumL[j])

# print(max(dp))