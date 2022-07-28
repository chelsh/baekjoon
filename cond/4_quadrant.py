x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)


print([3,2,4,1][int(x>0)*2 + int(y>0)])