M, N = [int(i) for i in input().split()]

def primeNum(n):
    prime_list = [2]
    num = 3
    while num <= n:
        for i in prime_list:
            if num % i == 0:
                num += 1
            