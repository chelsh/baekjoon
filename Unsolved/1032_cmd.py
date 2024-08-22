import sys

N = int(sys.stdin.readline())

L = []
for _ in range(N):
    L.append(sys.stdin.readline().strip())

result = ""
for i in range(len(L[0])):
    result += L[0][i]

for i in range(1, N):
    for j in range(len(L[0])):
        if L[i][j] != L[0][j]:
            result = result[:j] + '?' +  result[j+1:]

print(result)