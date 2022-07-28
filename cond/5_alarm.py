time = input()
t = time.split()
H = int(t[0])
M = int(t[1])
if M >= 45:
    M -= 45
    print(H, M)
else:
    if H == 0:
        H = 23
        M += 15
        print(H, M)
    else:
        H -= 1
        M += 15
        print(H, M)