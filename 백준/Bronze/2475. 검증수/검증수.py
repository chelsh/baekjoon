import sys

nums = [int(n) for n in sys.stdin.readline().split()]
print(sum(list(map(lambda n : n ** 2, nums))) % 10)
