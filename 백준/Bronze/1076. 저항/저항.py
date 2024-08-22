import sys


colors = []
for _ in range(3):
    colors.append(sys.stdin.readline().strip())

L = [0, 0, 0]
for i in range(3):
    if colors[i] == 'black':
        L[i] = 0
    elif colors[i] == 'brown':
        L[i] = 1
    elif colors[i] == 'red':
        L[i] = 2
    elif colors[i] == 'orange':
        L[i] = 3
    elif colors[i] =='yellow':
        L[i] = 4
    elif colors[i] =='green':
        L[i] = 5
    elif colors[i] == 'blue':
        L[i] = 6
    elif colors[i] == 'violet':
        L[i] = 7
    elif colors[i] == 'grey':
        L[i] = 8
    elif colors[i] == 'white':
        L[i] = 9

result = (L[0] * 10 + L[1]) * (10 ** L[2])
print(result)