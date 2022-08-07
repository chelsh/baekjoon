T = int(input())
d = {}
for i in range(1,T+1):
    num = input()
    A,B = num.split()
    d[i] = A+" + "+B+" = "+str(int(A) + int(B))
for i in d:
    print("Case #{0}: {1}".format(i, d[i]))