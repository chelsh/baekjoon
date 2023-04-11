x = True
l = []
while x == True:
    case = input()
    if case == "0 0":
        x = False
    else:
        a,b = case.split()
        l.append(int(a)+int(b))
for i in l:
    print(i)