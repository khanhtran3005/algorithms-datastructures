def atm(coins, withdraw):
    coinUsed = {}

    for coin, amount in coins.items():
        coin = int(coin)

        if withdraw == 0:
            break
        if withdraw < coin:
            continue

        coinsNeeded = withdraw // coin

        if coinsNeeded <= amount:
            coinUsed[str(coin)] = coinsNeeded
            withdraw = withdraw - coin * coinsNeeded

        else:
            coinUsed[str(coin)] = amount
            withdraw = withdraw - coin * amount

    if withdraw > 0:
        print("Not enough money!")
    else:
        print(coinUsed)


coins = {"100": 8, "20": 200}

atm(coins, 1020)
