def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0;b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

print(fibo(int(input())))