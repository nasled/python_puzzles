
dict = {0: 0, 1: 1, 2: 2, 3: 4}
def counter(n):
    if n in dict.keys():
        return dict.get(n)

    result = counter(n-1) + counter(n-2) + counter(n-3)
    dict.update({n: result})
    return dict.get(n)

# print(counter(5))
# print(counter(6))
# print(counter(7))


# def dict_counter(dict, n):
#     if n in dict.keys():
#         return dict, dict.get(n)
#
#     result = dict_counter(dict, n - 1) + dict_counter(dict, n - 2) + dict_counter(dict, n - 3)
#     dict.update({n: result})
#     return dict, dict.get(n)
#
# def counter(n):
#     dict, n = dict_counter({0: 0, 1: 1, 2: 2, 3: 4}, n)
#     return n
#
#
# print(counter(5))
# print(counter(dict, 6))
# print(counter(dict, 7))


def make_change(coins, n):
    results = [0 for _ in range(n + 1)]
    results[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            results[i] += results[i - coin]
    return results[n]

# print(make_change([2, 5, 3, 6], 10))
# print(make_change([1, 2, 3], 6))
# print(make_change([1, 2, 3], 7))