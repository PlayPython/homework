'''
@author Sheldon Yan
:copyright: (c) 2018 by Sheldon
:license: Apache 2.0, see LICENSE for more details.
'''
import math
# 使用循环和算数运算，生成0到20的偶数
# - 使用循环和算数运算，生成0到20的奇数
# - 写一个函数，判断一个数是否被另外一个数整除
# - 判断一个数字是否为素数
# - 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N
# <= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N对它们排序，然后显示这个子集。
import random

print([i for i in range(21) if i % 2 == 0])

print([i for i in range(21) if i % 2])


def judge_exact_division(first_number, second_number):
    first_number, second_number = int(first_number), int(second_number)
    if first_number % second_number == 0:
        return True
    else:
        return False


def judge_prime_number(number):
    number = int(number)
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True


def sorted_n_list():
    a_list = [random.randrange(0, 2 ** 31 - 1) for i in range(0, random.randint(1, 100))]
    return sorted(a_list)


if __name__ == '__main__':
    print(judge_exact_division(9, 4))
    print(sorted_n_list())
    print(judge_prime_number(2))
    print(judge_prime_number(9))
    print(judge_prime_number(99))
    print(judge_prime_number(100))
    print(judge_prime_number(97))
