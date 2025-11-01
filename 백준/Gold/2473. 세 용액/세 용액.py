import sys

N = int(sys.stdin.readline())
a = sorted(map(int, sys.stdin.readline().split()))

best = float('inf')
ans = (0, 0, 0)

for i in range(N - 2):
    l, r = i + 1, N - 1
    while l < r:
        s = a[i] + a[l] + a[r]
        if abs(s) < best:
            best = abs(s)
            ans = (a[i], a[l], a[r])
            if s == 0:  # 더 이상 개선 불가
                print(*ans)
                sys.exit(0)
        if s < 0:
            l += 1
        else:
            r -= 1

print(*ans)
