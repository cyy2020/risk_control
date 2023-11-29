def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def nth_mersenne_number(n):
    count = 0
    number = 2
    while True:
        if is_prime(number):
            mersenne_number = 2 ** number - 1
            if is_prime(mersenne_number):
                count += 1
                if count == n:
                    return mersenne_number
        number += 1


n = 5
result = nth_mersenne_number(n)
print(f"The {n}th Mersenne number is {result}")
