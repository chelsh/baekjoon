s = set()
for i in range(10):
    i = int(input()) % 42
    s.add(i)
print(len(s))