# x = True
# l = []
# while x == True:
#     case = input()
#     if case == "":
#         x = False
#     else:
#         A,B = case.split()
#         l.append(int(A)+int(B))
# print("\n".join(str(i) for i in l))
while True:
    n = input()
    A,B = n.split()
    print(int(A)+int(B))