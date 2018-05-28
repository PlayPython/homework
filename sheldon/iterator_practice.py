# 用yield构造一个返回质数函数，从2开始，每次调用返回下一个更大的质数
import itertools


# 判断是否是质数
def is_prime(num):
    for n in range(2, (num) // 2 + 1):
        if num % n == 0:
            return False
    return True


# 构造质数生成器
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
