N = int(input())
hansu_list = []
def hansu(x):
    l = [int(i) for i in list(str(x))]
    dl = []
    for j in range(len(l) - 2):
        d = l[j] - l[j + 1]
        print(d)
        dl.append(d)
    print(dl)
    set_dl = set(dl)
    if len(set_dl) == 1:
        return x
for x in range(1, N+1):
    hansu_list.append(hansu(x))
print(len(hansu_list))
hansu(12)