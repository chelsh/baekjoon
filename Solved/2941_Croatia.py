croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
def cro_alphabet(S):
    cnt = 0
    for s in croatia:
        if s in S:
            cnt += S.count(s)
            S = S.replace(s, " ")
    cnt += len(S.replace(" ", ""))
    return cnt
print(cro_alphabet(input()))

# s = input().replace("c=","*").replace("c-","*").replace("dz=","*").replace("d-","*").replace("lj","*").replace("nj","*").replace("s=","*").replace("z=","*")
# print(len(s))