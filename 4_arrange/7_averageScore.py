C = int(input())
for i in range(C):
    scores = input()
    score_list = scores.split()
    l = [int(x) for x in score_list]
    N = l[0]
    l = l[1:]
    average = sum(l)/N
    student = 0
    for x in l:
        if x > average:
            student += 1
    print(student/N)