N = int(input())
OX_list = []
for i in range(N):
    OX_list.append(input())

# for x in OX_list:
#     score = 0
#     t = x.index("O")
#     for n in range(len(x[t:])):
#         if x[t+n] == "O":
#             score += 1
#         else:
#             x = x[t+n+1:]
#             t = x.index("O")
#     print(score)

for x in OX_list:
    score = 0
    score += x.count("O")
    for n in range(len(x)-x.index("O")):
        if x[x.index("O")+n] == "O":
            score += n
        else:
            x = x[x.index("O")+n:]