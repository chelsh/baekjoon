C = int(input())
percent_list = []
for i in range(C):
    sl = [int(x) for x in input().split()]  #score_list
    N = sl[0]
    sl = sl[1:]
    average = sum(sl)
    superior = 0
    for n in sl:
        if n*N > average:
            superior += 1
    
    rate = superior/N *100
    # percent_list.append(f'{rate:.3f}%')

    percent = str(round(rate*1000)) 
    if percent == "0":
        percent_list.append("0.000%")
    else:
        percent_list.append(percent[:-3] + "." + percent[-3:] + "%")
for s in percent_list:
    print(s)