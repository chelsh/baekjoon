stack = []
top = -1

k = int(input())
for _ in range(k):
    n = int(input())
    if n == 0 and top != -1:
        stack.pop()
        top -= 1
    elif n != 0:
        stack.append(n)
        top += 1
    
print(sum(stack))