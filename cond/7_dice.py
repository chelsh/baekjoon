dice = input()
d = dice.split()
a = int(d[0])
b = int(d[1])
c = int(d[2])

if a == b == c:
    print(10**4 + a*10**3)
elif a != b and a != c and b != c:
    l = [a,b,c]
    l.sort()
    print(l[2]*100)
else:
    if a == b:
        print(10**3 + a*100)
    elif b == c:
        print(10**3 + b*100)
    else:
        print(10**3 + c*100)