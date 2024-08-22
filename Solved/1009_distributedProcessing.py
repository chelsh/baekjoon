import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = sys.stdin.readline().split()

    if a[-1] == '1':
        print(1)
    if a[-1] == '2': 
        b = b[-2:]
        idx = int(b) % 4
        if idx == 1:
            print(2)
        if idx == 2:
            print(4)
        if idx == 3:
            print(8)
        if idx == 0:
            print(6)
    if a[-1] == '3':
        b = b[-2:]
        idx = int(b) % 4
        if idx == 1:
            print(3)
        if idx == 2:
            print(9)
        if idx == 3:
            print(7)
        if idx == 0:
            print(1)
    if a[-1] == '4': 
        b = b[-1]
        idx = int(b) % 2
        if idx == 0:
            print(6)
        if idx == 1:
            print(4)
    if a[-1] == '5': 
        print(5)
    if a[-1] == '6': 
        print(6)
    if a[-1] == '7': 
        b = b[-2:]
        idx = int(b) % 4
        if idx == 1:
            print(7)
        if idx == 2:
            print(9)
        if idx == 3:
            print(3)
        if idx == 0:
            print(1)
    if a[-1] == '8': 
        b = b[-2:]
        idx = int(b) % 4
        if idx == 1:
            print(8)
        if idx == 2:
            print(4)
        if idx == 3:
            print(2)
        if idx == 0:
            print(6)
    if a[-1] == '9': 
        b = b[-1]
        idx = int(b) % 2
        if idx == 0:
            print(1)
        if idx == 1:
            print(9)
    if a[-1] == '0': 
        print(10)


# 2 - 2 4 8 6
# 3 - 3 9 7 1
# 4 - 4 6
# 5 - 5
# 6 - 6
# 7 - 7 9 3 1
# 8 - 8 4 2 6
# 9 - 9 1
# 0 - 0