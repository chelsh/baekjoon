num = input()
n = num.split()
A = int(n[0])
B = int(n[1])
C = int(n[2])
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)