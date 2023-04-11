def init(n):
    l = [int(x) for x in list(str(n))]
    return n + sum(l)
nums = [n for n in range(1,10001)]
for i in range(10000):
    if init(i) in nums:
        nums.remove(init(i))
    else:
        pass
for i in nums:
    print(i)