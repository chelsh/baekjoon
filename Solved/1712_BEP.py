# from sympy import*
# import sympy as sp
# abc = input()
# l = [int(i) for i in abc.split()]
# A,B,C = l[0],l[1],l[2]
# x = sp.symbols("x")
# n = 0
# def avenue(x):
#     return C*x - (A + B*x)
# if limit(avenue(x), x, sp.oo) == oo:
#     while avenue(n) < 0:
#         n += 1
#     if avenue(n+1) > 0:
#         print(n+1)
#     elif avenue(n+1) == 0:
#         print(n+2)
# else:
#     print(-1)

abc = input()
l = [int(i) for i in abc.split()]
A,B,C = l[0],l[1],l[2]
if C > B:
    print(int(A / (C - B)) + 1)
else:
    print(-1)