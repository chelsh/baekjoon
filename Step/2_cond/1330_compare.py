s = input()
d = s.split(" ")
A = int(d[0])
B = int(d[1])
if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")