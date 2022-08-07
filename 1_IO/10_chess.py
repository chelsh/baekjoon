white = input()
l = [int(i) for i in white.split()]
list = [1 - l[0], 1 - l[1], 2 - l[2], 2 - l[3], 2 - l[4], 8 - l[5]]
for j in list:
    print(j, end = " ")