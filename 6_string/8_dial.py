str = list(input())
import string
upper_list = list(string.ascii_uppercase)
time = []
for i in str:
    for n in range(7):
        if i in upper_list[3*n:3*n+3]:
            x = n + 3
            time.append(x)
    if i in upper_list[21:26]:
        x = 10
        time.append(x)
print(sum(time))