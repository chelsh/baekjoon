def wavefront(n):
    sq = [[1,1,1,2,2,3]]

    if n <= 6:
        return sq[0][n - 1]
    
    else:
        q = n // 6
        r = n % 6
        for i in range(q):
            sq.append([sq[i][1]+sq[i][5]])

            for j in range(4):
                sq[i + 1].append(sq[i + 1][j] + sq[i][j + 2])

            sq[i + 1].append(sq[i + 1][0] + sq[i + 1][4])

        if r == 0:
            return sq[q - 1][5]
        else:
            return sq[q][r - 1]


T = int(input())
for _ in range(T):
    print(wavefront(int(input())))