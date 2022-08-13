N = int(input())
OX_list = []
for i in range(N):
    OX_list.append(input())
for s in OX_list:
    box = 0
    score = 0
    for c in s:
        if c == "O":
            box += 1
            score += box
        if c == "X":
            box = 0
    print(score)