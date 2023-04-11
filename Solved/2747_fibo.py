n = int(input())

a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)

#재귀쓰면 시간초과