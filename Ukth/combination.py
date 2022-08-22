def comb(arr, n):
    result = []

    if len(arr) < n:
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]]+ j)
    return result


L = [1, 2, 3, 4, 5, 6, 7]
print(comb(L, 3))