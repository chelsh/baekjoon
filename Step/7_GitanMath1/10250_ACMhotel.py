T = int(input())

def ACM(h, n):
    floor = n % h
    room_num = n // h + 1
    if floor == 0:
        floor = h
        room_num -= 1
    print(str(floor) + str(room_num).rjust(2, "0"))


for i in range(T):
    H, W, N = [int(x) for x in input().split()]
    ACM(H, N) 