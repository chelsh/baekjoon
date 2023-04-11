# set에서는 in 연산의 시간복잡도가 평균 O(1) -> list와 비교했을때 시간복잡도 낮음

N = int(input())
A = set(int(n) for n in input().split())
M = int(input())
B = [int(n) for n in input().split()]

for n in B:
    if n in A:
        print(1)
    else:
        print(0)






#시간초과난 코드 (binary serach)

# def findNum(L, n):
#     L.sort()

#     while len(L) != 1:
#         m = len(L) // 2
#         if n < L[m]:
#             L = L[:m]
#         else:
#             L = L[m:]

#     if n == L[0]:
#         return 1
#     else:
#         return 0


# N = int(input())
# A = [int(n) for n in input().split()]
# M = int(input())
# B = [int(n) for n in input().split()]

# for n in B:
#     print(findNum(A, n))