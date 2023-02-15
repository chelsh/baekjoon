T = int(input())
l = []
for i in range(1,T+1):
    num = input()
    n = num.split()
    A = int(n[0])
    B = int(n[1])
    l.append(A+B)
    i += 1
for i in range(T):
    print(l[i])