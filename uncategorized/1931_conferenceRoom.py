import sys

N = int(sys.stdin.readline())

if N == 1:
    print(1)

else:
    L = []
    for _ in range(N):
        L.append([int(n) for n in sys.stdin.readline().split()])

    L.sort(key= lambda x: (x[1], x[0]))



    result = [L[0]]
    end = L[0][1]

    for i in range(1, N):
        if end <= L[i][0]:
            result.append(L[i])
            end = L[i][1]

  
    print(len(result))













# #중첩 회의 적은 순서 (시간초과 / 되나?)
# L = []
# for _ in range(N):
#     L.append([int(n) for n in sys.stdin.readline().split()])

# for i in range(N):
#     overlap = 0
#     for cnf in L:
#         if L[i][2] == 0:
#             if cnf[0] < L[i][0] < cnf[1]:
#                 overlap += 1
#                 break
#         else:        
#             if cnf[0] <= L[i][0] < cnf[1] or cnf[0] < L[i][1] <= cnf[1]:
#                 break
#     else:








#사용 시간 적은 순서 (실패)
# L = []
# for _ in range(N):
#     cnf = [int(n) for n in sys.stdin.readline().split()]
#     cnf.append(cnf[1] - cnf[0])
#     L.append(cnf)
    
# L.sort(key = lambda x: x[2])

# use = []
# result = 0
# for i in range(N):
#     for cnf in use:
#         if L[i][2] == 0:
#             if cnf[0] < L[i][0] < cnf[1]:
#                 break
#         else:        
#             if cnf[0] <= L[i][0] < cnf[1] or cnf[0] < L[i][1] <= cnf[1]:
#                 break
#     else:
#         use.append(L[i])
#         result += 1

# print(result)