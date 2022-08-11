C = int(input())
percent_list = []
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
    percent_list.append(str(round(student/N*100, 3))+"%")
for s in percent_list:
    print(s)