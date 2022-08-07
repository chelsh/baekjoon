A = int(input())
B = int(input())
C = int(input())
n = str(A*B*C)
for i in range(10):
    print(n.count(str(i)))