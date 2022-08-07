T = int(input())
test_case = []
for i in range(T):
    test_case.append(input())
for x in test_case:
    a,b = x.split()
    a = int(a)
    str_list = list(b)
    for y in str_list:
        print(y*a, end = "")
    print()