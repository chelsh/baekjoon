n = int(input())
def fibo(x):
    if x < 2:
        return x
    else:
        return fibo(x-2) + fibo(x-1)
print(fibo(n))