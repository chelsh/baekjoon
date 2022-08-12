L = [1,3,2,5,8,2,1]

def max_L(L): # find maximum value of L
    max = L[0]
    for item in L:
        if max < item:
            max = item
    return max

def min_L(L): # min
    min = L[0]
    for item in L:
        if min > item:
            min = item

    return min

def sum_L(L): # sum of L
    sum = 0
    for item in L:
        sum += item
    return sum

def find_L(L, n): # if n exist in L
    for item in L:
        if item == n:
            return True
    return False
    
def find_lt(L, n): # count number less than n in L
    cnt = 0
    for item in L:
        if item < n:
            cnt += 1
    return cnt

print(max_L(L))
print(min_L(L))
print(sum_L(L))
print(find_L(L, 1))
print(find_lt(L, 5))