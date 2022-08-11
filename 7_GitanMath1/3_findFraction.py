X = int(input())
n = 1
while X > n:
    X -= n
    n += 1
if n % 2 == 0:
    print(str(X)+"/"+str(n - (X - 1)))
else:
    print(str(n - (X - 1))+"/"+str(X))