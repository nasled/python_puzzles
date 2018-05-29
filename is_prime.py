
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        for i in range(3, int(num**(1/2.0)) + 1, 2):
            if num % i == 0:
                return False

    return True

# print(is_prime(3))
# print(is_prime(12))
# print(is_prime(5))
# print(is_prime(7))
# print(is_prime(31))
# print(is_prime(33))
