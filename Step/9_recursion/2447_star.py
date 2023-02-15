def printer(L):
    for line in L:
        print("".join(line))

L = [[ " " for i in range(27) ] for j in range(27) ]

def draw_fact(ind1, ind2): # ind1 = [0,0], ind2 = [27,27]

    if ind2[0] - ind1[0] == 1:
        L[ind1[0]][ind1[1]] = "*"
        return

    X1 = ind1[0]
    Y1 = ind1[1]

    X2 = ind2[0]
    Y2 = ind2[1]

    x_1 = (2 * X1 + X2)/3
    x_2 = (X1 + 2 * X2)/3

    y_1 = (2 * Y1 + Y2)/3
    y_2 = (Y1 + 2 * Y2)/3

    draw_fact([X1, Y1], [x_1, y_1])
    draw_fact([x_1, Y1], [x_2, y_1])
    draw_fact([x_2, Y1], [X2, y_1])

    draw_fact([X1, y_1], [x_1, y_2])
    draw_fact([x_2, y_1], [X2, y_2])

    draw_fact([X1, y_2], [x_1, Y2])
    draw_fact([x_1, y_2], [x_2, Y2])
    draw_fact([x_2, y_2], [X2, Y2])

draw_fact([0,0], [27,27])


printer(L)