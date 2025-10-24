import sys

A,B,C = [sys.stdin.readline().strip() for _ in range(3)]
a,b,c = [int(s) for s in [A,B,C]]

print(a+b-c)
print(int(A+B)-c)