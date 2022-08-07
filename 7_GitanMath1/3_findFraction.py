X = int(input())
def find_fraction(x):
    m = x // 2
    n = x % 2
    if n == 0:
        print(str(m)+'/'+str(2))
    if n == 1:
        print(str(m+1)+'/'+str(1))
find_fraction(X)