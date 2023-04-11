def fiboZeroOne(n):
    if n == 0:
        return "1 0"
    elif n == 1:
        return "0 1"
    elif n == 2:
        return "1 1"
    elif n == 3:
        return "1 2"
    else:
        za = 1;zb = 1;oa = 1;ob = 2
        for _ in range(n - 3):
            za, zb = zb, za + zb
            oa, ob = ob, oa + ob
        return str(zb) + ' ' + str(ob)

for _ in range(int(input())):
    print(fiboZeroOne(int(input())))