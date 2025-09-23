import sys

L = int(sys.stdin.readline())
S = [int(n) for n in sys.stdin.readline().split()]
n = int(sys.stdin.readline())

S.sort()
S.insert(0, 0)

a = 0
b = 0

for i in range(len(S)-1):
    if S[i] < n and n < S[i+1]:
        a, b = S[i], S[i+1]

if a == 0 and b == 0:
    print(0)
else:
    result = (n-a-1)*(b-n-1) + (n-a-1)+(b-n-1)
    print(result)
