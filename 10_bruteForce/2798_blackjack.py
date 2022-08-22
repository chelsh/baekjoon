N, M = [int(n) for n in input().split()]
cards = [int(n) for n in input().split()]


















# def blackjack(n, m, l):
#     pick_sum = []
#     for i in range(N):
#         pick = []
#         pick.append(cards[i])
#         print("a")
#         print(pick)

#         for i in range(N - 1):
#             pick.append(cards[i + 1])
#             print("b")
#             print(pick)

#             for i in range(N - 2):
#                 pick.append(cards[i + 2])
#                 print("c")
#                 print(pick)
#                 pick_sum.append(sum(pick))
#                 pick.pop()
#             pick.pop()
#     print(pick_sum)
#     for item in pick_sum:
#         if item >= M:
#             pick_sum.remove(item)
#     print(max(pick_sum))

# blackjack(N, M, cards)