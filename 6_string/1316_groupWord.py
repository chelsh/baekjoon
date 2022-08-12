N = int(input())
L = []
group_words = 0
for i in range(N):
    L.append(list(input()))
for s in L:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            s[i] = " "
    s = "".join(s).replace(" ", "")
    if len(set(s)) == len(s):
        group_words += 1
print(group_words)