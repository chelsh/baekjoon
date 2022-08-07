import string
S = input()
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
for s in alphabet_list:
    if s in S:
        print(S.index(s))
    else:
        print(-1)