import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

# 산술평균
avg = sum(nums) / N
if avg >= 0:
    print(int(avg + 0.5))
else:
    print(int(avg - 0.5))

# 중앙값
nums.sort()
print(nums[int((N-1)/2)])

# 최빈값
counter = Counter(nums)
max_freq = max(counter.values())
max_freq_nums = [key for key, value in counter.items() if value == max_freq]
max_freq_nums.sort()
if len(max_freq_nums) > 1:
	print(max_freq_nums[1])
else:
	print(max_freq_nums[0])

# 범위
print(nums[-1] - nums[0])