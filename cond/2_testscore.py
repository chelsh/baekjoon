score = int(input())
if 90 <= score:
    print("A")
elif 80 <= score:
    print("B")
elif 70 <= score:
    print("C")
elif 60 <= score:
    print("D")
else:
    print("F")

print("F" if score < 60 else ("A" if score == 100 else "DCBA"[(score-60)//10]))