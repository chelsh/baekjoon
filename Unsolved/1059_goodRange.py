import sys

L = int(sys.stdin.readline())
S = [int(n) for n in sys.stdin.readline().split()]
n = int(sys.stdin.readline())

def sol(set, num):
    if num in set:
        print(0)
        return

    set.append(num)
    set.sort()

    idx = set.index(num)

    if idx == 0:
        print(set[1] - n - 1)
        return

    if idx == len(set) - 1:
        print(n - set[-2] - 1)
        return

    min, max = set[idx-1] + 1, set[idx+1] - 1

    if min == max:
        print(0)
        return

    print((num - min) * (max - num) + max - min)

sol(S, n)