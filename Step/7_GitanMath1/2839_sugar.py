N = input()
def deliver_sugar(n):
    if n[-1] == 0 or n[-1] == 5:
        return int(n) // 5
    else:
        n = int(n)
        cnt = 0
        while n % 5 != 0:
            n -= 3
            cnt += 1
            if n < 0:
                return -1
        cnt += n // 5
        return cnt
print(deliver_sugar(N))