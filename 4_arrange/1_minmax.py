N = input()
integer = input()
num_list = integer.split()
l = [int(x) for x in num_list]
print(min(l), max(l))