X = int(input())
N = int(input())
l = []
for i in range(N):
    a, b = [int(x) for x in input().split()]
    l.append(a * b)
if X == sum(l):
    print('Yes')
else:
    print('No')