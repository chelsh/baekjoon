def selection_sort(arr):
    for i in range(len(arr)):
        idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

N = int(input())
L = []
for _ in range(N):
    L.append(int(input()))

for n in selection_sort(L):
    print(n)