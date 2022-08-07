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
    try:
        n = input()
        A,B = n.split()
        print(int(A)+int(B))
    except:
        break



# f = open("./input.txt")
# while True:
#     inp = f.readline()
#     print(inp,123)
#     inp = inp.split()
#     if not inp:
#         break
#     print(int(inp[0])+int(inp[1]))
