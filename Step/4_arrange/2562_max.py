i = 1
l = []
while i < 10:
    num = int(input())
    l.append(num)
    i += 1
m = max(l)
print(m)
print(l.index(m)+1)