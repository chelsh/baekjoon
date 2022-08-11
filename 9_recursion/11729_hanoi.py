N = int(input())

def hanoi(f, e, n):
    if n == 1:
        return [str(f)+" "+str(e)]

    m = 6 - (f + e)
    return hanoi(f, m, n - 1)+ hanoi(f, e, 1)+ hanoi(m, e, n - 1)

result = hanoi(1, 3, N)
print(len(result))
print("\n".join([str(i) for i in result]))