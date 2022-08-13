l = input()
N, X = l.split()
a = input()
A = a.split()
for x in A:
    if int(x) < int(X):
        print(x, end = " ")