import sys

N = int(sys.stdin.readline())

P = [int(n) for n in sys.stdin.readline().split()]
P.sort()

result = 0
for i in range(len(P)):
    result += sum(P[:i + 1])

print(result)