import sys

nums = [int(n) for n in sys.stdin.readline().split()]
length = len(nums)

L = []

for i in range(length - 2):
    for j in range(1, length - 1):
        for k in range(2, length):
            L.append(nums[i] + nums[j] + nums[k])

for 