import itertools


def is_prime(num):
    for n in range(2, (num) // 2 + 1):
        if num % n == 0:
            return False
    return True


def return_prime():
    num = 2
    yield num
    while True:
        num = num + 1
        if is_prime(num):
            yield num


if __name__ == '__main__':
    prime_ger = itertools.islice(return_prime(), 100)
    for item in prime_ger:
        print(item)
