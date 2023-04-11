def numChange(money):
    coins = [500, 100, 50, 10, 5, 1]
    result = 0
    money = 1000 - money
    for i in range(len(coins)):
        result += money // coins[i]
        money %= coins[i]
    return result

pay = int(input())
print(numChange(pay))