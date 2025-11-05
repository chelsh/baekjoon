import sys

input = sys.stdin.readline
write = sys.stdout.write

M = int(input())
s = set()

def sol(tokens):
    global s
    op = tokens[0]

    if op == "all":
        s = set(range(1, 21))
    elif op == "empty":
        s.clear()
    else:
        n = int(tokens[1])

        if op == "add":
            s.add(n)
        elif op == "remove":
            s.discard(n)
        elif op == "check":
            if n in s:
                write("1\n")
            else:
                write("0\n")
        elif op == "toggle":
            if n in s:
                s.remove(n)
            else:
                s.add(n)

for _ in range(M):
    sol(input().split())
