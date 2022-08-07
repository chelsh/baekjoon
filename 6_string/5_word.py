from itertools import count
import string
upper_list = list(string.ascii_uppercase)
lower_list = list(string.ascii_lowercase)
str = input()
count_list = []
for i in range(26):
    count_list.append(str.count(upper_list[i])+str.count(lower_list[i]))
m = max(count_list)
mi = count_list.index(m)
if count_list.count(m) == 1:
    print(upper_list[mi])
else:
    print("?")