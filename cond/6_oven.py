time = input()
t = time.split()
A = int(t[0])
B = int(t[1])
cook = input()
C = int(cook)

mnt = ((A*60+B+C) % (60*24))
print (mnt//60, mnt%60)

if B+C <= 59:
    print(A, B+C)
else:
    A += (B+C)//60
    if A >= 24:
        print(A-24, (B+C)%60)
    else:
        print(A, (B+C)%60)


mnt = (A*60+B+C % 60*24)
print (mnt//60, mnt%60)