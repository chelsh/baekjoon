import sys

def lotto(T):
    k = T[0]
    S = T[1:]

    L = [0,1,2,3,4,5]

    

    


while True:
    T = [int(n) for n in sys.stdin.readline().split()]
    print(T)
    if T == [0]:
        break
    else:
        lotto(T)
