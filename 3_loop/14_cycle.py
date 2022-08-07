N = input()
if len(N) == 1:
    N = "0" + N
a = int(N[0]) + int(N[1])
b = N[1]
n = b + str(a)[-1]
cycle = 1
while n != N:
    a = int(n[0]) + int(n[1])
    b = n[1]
    n = b + str(a)[-1]
    cycle += 1
print(cycle)