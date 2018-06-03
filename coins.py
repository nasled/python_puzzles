

def get_number(coins, money):
    storage = [0 for i in range(money+1)]
    storage[0] = 1
    for coin in coins:
        for j in range(coin, len(storage)):
            storage[j] += storage[j - coin]
    return storage[money]

print(get_number([1,2,3], 4))
print(get_number([2,5,3,6], 10))