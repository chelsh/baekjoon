N = int(input())

def hanoi(f, e, n):
    if n == 1:
        return [str(f)+" "+str(e)]
    l = []
    m = 6 - (f + e)
    l += hanoi(f, m, n - 1)
    l += (hanoi(f, e, 1))
    l += (hanoi(m, e, n - 1))
    return l
print(len(hanoi(1, 3, N)))
print("\n".join([str(i) for i in hanoi(1, 3, N)]))