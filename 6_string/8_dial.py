str = list(input())
import string
upper_list = list(string.ascii_uppercase)
time = 0

for c in str:
    for n in range(5):
        if c in upper_list[3*n:3*n+3]:
            time += n + 3
    if c in upper_list[15:19]:
        time += 8
    if c in upper_list[19:22]:
        time += 9
    if c in upper_list[-4:]:
        time += 10
nums = "22233344455566677778889999"

sum([int(nums[ord(c)-65]) for c in str])
print(time)