# # 数值类型练习
# -使用循环和算数运算，生成0到20的偶数
# -使用循环和算数运算，生成0到20的奇数
def judge_num():
    for i in range(21):
        if i / 2 == 0:
            print("偶数{0}".format(i))
        else:
            print("奇数{0}".format(i))


# - 写一个函数，判断一个数是否被另外一个函数整除

def func(x, y):
    if x % y == 0:
        print("可以被整除")
    else:
        print("无法被整除")


# - 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1 < N <= 100）和（0 <= n <= 2 ** 31 - 1）。然后再随机从这个列表中取N（1 <= N <= 100）个随机数出来，对它们排序，然后显示这个子集。

import random


def rand_num():
    N = random.randint(2, 100)
    L = []
    for i in range(N):
        n = random.randint(0, 2 ** 31 - 1)
        L.append(n)
    return L.sort()


# 字符串和列表
# -创建一个函数，除去字符串前面和后面的空格

def func0(s):
    return s.strip()


# -输入一个字符串，判断是否为回文


def func1(s):
    s1 = s[::-1]
    if s1 == s:
        return True
    else:
        return False


# - 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty - nine，限定值在0~100

# - 给出两个可以识别格式的日期，比如MM / DD / YY 或者DD / MM / YY计算两个日期的相隔天数
from datetime import datetime


def day1_day2(day1, day2):
    """
    :param day1: 30/12/2017
    :param day2: 13/02/2018
    :return: days
    """
    day1 = datetime.strptime(day1, "%d/%m/%Y")
    day2 = datetime.strptime(day2, "%d/%m/%Y")
    days = day1 - day2
    return days


# 字典和集合练习
# -创建一个字典，把字典中的键按照字母顺序显示出来
dict_p1 = {"z": "z1", "b": "b1", "c": "c1", "m": "b2"}


def dict_keys_sort():
    m = list(dict_p1.keys())
    m.sort()
    return m


#  -根据已经排序好的字母的键，显示这个字典中的键和值

def dict_keys_values_sort():
    for i in dict_keys_sort():
        print("key:{0}-->value:{1}".format(i, dict_p1[i]))


# 使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A | B和A & B
def random_A_B():
    pass


# 文件和条件语句练习
# - 文件过滤，显示一个文件的所有行，忽略以  # 开始的行
def read_txt_ignore(path):
    with open(path, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            line01 = line.rstrip()
            if line01 and line01.lstrip()[0] != "#":
                print(line01)
            elif line01 == "":
                print(line01)
            line = f.readline()


# - 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
def compare(pathA, pathB):
    fA = open(pathA, 'r', encoding='utf-8')
    fB = open(pathB, 'r', encoding='utf-8')
    lineA = fA.readline()
    lineB = fB.readline()
    n = 0
    while lineA and lineB:
        n = n + 1
        if lineA != lineB:
            for i in range(len(lineA)):
                if lineA[i] != lineB[i]:
                    print("文件A的行数:{0}，A的列数:{1}".format(n, i + 1))
                    break
            break
        lineA = fA.readline()
        lineB = fB.readline()


# - 写一个函数，返回N的阶乘
def N_factorial(n):
    m = 1
    while n > 1:
        m = m * n
        n = n - 1
    return m


# - 判断一个数字是否为素数



# - 统计一个文本中每个单词出现个数
if __name__ == "__main__":
    # compare(r'D:\123.txt', r'D:\1234.txt')
    print(N_factorial(4))
