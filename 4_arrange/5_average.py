N = int(input())
score = input()
l = score.split()
l = [int(x) for x in l]
m = (max(l))
new_score = [i/m*100 for i in l]
print(sum(new_score)/len(new_score))