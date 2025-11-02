import sys

a = [sys.stdin.readline() for _ in range(3)]

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

ans = 0
for i in range(3):
	if is_integer(a[i]):
		a[i] = int(a[i])
		ans = a[i] + (3-i)
if ans % 3 == 0 and ans % 5 == 0:
	print("FizzBuzz")
elif ans % 3 == 0:
	print("Fizz")
elif ans % 5 == 0:
	print("Buzz")
else:
	print(ans)
