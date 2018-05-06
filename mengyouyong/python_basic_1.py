import random
import math
import time
import collections

# 打印π
print(math.pi)
##数值类型练习
# - 使用循环和算数运算，生成0到20的偶数
for i in range(0, 21, 2):
    print(i)

# - 使用循环和算数运算，生成0到20的奇数
for i in range(1, 21, 2):
    print(i)


# - 写一个函数，判断一个数是否被另外一个数整除
def divide_exactly(x, y):
    if x % y == 0:
        print("yes")
    else:
        print("no")


divide_exactly(8, 2)
'''
- 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N
<= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N（1<=N<=100）个
随机数出来，对它们排序，然后显示这个子集。
备注：就是在将这个列表排个序；
'''


def random_list():
    N = random.randrange(1, 101, 1)
    list = []
    for i in range(N):
        n = random.randrange(0, 2 ** 31, 1)
        list.append(n)
    print(sorted(list))
    print(N)


random_list()
"""
#字符串和列表
- 创建一个函数，除去字符串前面和后面的空格
- 输入一个字符串，判断是否为回文
- 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
- 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
"""


# - 创建一个函数，除去字符串前面和后面的空格
def Remove_Spaces(string):
    print(string.strip())


Remove_Spaces(" jijijisi   ")


# - 输入一个字符串，判断是否为回文
def Palindrome():
    s = input("请输入一个回文字符")
    li = list(s)
    li1 = li.copy()
    li1.reverse()
    if li == li1:
        print("您输入的是回文字符")
    else:
        print("您输入的不是回文字符")


# - 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
def Translation(num):
    dict1 = {0: 'zero,', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
             9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen ', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
             18: 'eighteen', 19: 'nineteen '}
    dict2 = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
             90: 'ninety'}
    if num >= 0 and num < 20:
        for i in dict1.keys():
            if num == i:
                print(dict1.get(num))
    elif num >= 20 and num < 100 and num % 10 == 0:
        for i in dict2.keys():
            if num == i:
                print(dict2.get(num))
    elif num >= 20 and num < 100 and num % 10 != 0:
        x = num % 10
        y = num // 10 * 10
        for i in dict1.keys():
            if x == i:
                str1 = dict1.get(x)
        for i in dict2.keys():
            if y == i:
                str2 = dict2.get(y)
        print("{0}-{1}".format(str2, str1))
    elif num == 100:
        print('one hundred')
    else:
        print('请输入0到100之间的整数')


Translation(101)


# - 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
def Comput_Date(date1, date2):
    a = " 00:00:00"
    s = int(time.mktime(time.strptime(date1 + a, "%Y-%m-%d %H:%M:%S"))) - int(
        time.mktime(time.strptime(date2 + a, "%Y-%m-%d %H:%M:%S")))
    y = s // 24 // 3600
    if y >= 0:
        print("日期差为{0}天".format(y))
    else:
        print("日期差为{0}天".format(-y))


Comput_Date("2018-4-8", "2018-4-3")

'''
#字典和集合练习
- 创建一个字典，把字典中的键按照字母顺序显示出来
- 根据已经排序好的字母的键，显示这个字典中的键和值
'''


def Dict_Key_Sort(dict1):
    sort_key = sorted(dict1.keys())
    print(sort_key)  # 创建一个字典，把字典中的键按照字母顺序显示出来
    li = sort_key.copy()
    dict2 = {}
    for i in li:
        sort_key.append(dict1.get(i))  # 将字典的键和值组成一个列表
    for j in range(len(li)):
        dict2[sort_key[j]] = sort_key[j + len(li)]  # 通过生成新字典的方法将原字典按照已排序的键进行重新组合
    print(dict2)  # 根据已经排序好的字母的键，显示这个字典中的键和值


Dict_Key_Sort({"H": "我是H的值", "D": "我是D的值", "S": "我是S的值", "A": "我是A的值", "F": "我是F的值", "B": "我是B的值"})


# - 使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
def Random_Number():
    a = random.randrange(0, 9, 1)
    b = random.randrange(0, 9, 1)
    print(a | b, a & b)


Random_Number()

"""
#文件和条件语句练习
- 文件过滤，显示一个文件的所有行，忽略以#开始的行
- 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
- 写一个函数，返回N的阶乘
- 判断一个数字是否为素数
- 统计一个文本中每个单词出现个数

"""

# - 文件过滤，显示一个文件的所有行，忽略以#开始的行
with open("./test.txt", "r") as f:
    for eachline in f.readlines():
        if str(eachline)[0] == "#":
            continue
        else:
            print(eachline, end='')


# - 写一个函数，返回N的阶乘
def Return_Factorial(N):
    sum = 1
    for i in range(1, N + 1):
        sum = i * sum
    print(sum)


Return_Factorial(7)


# - 判断一个数字是否为素数
def Prime_Number(prime_number):
    number1 = 0
    for i in range(1, prime_number + 1):
        if prime_number % i == 0:
            number1 += 1
        else:
            pass
    if number1 == 2:
        print("{0}是素数".format(prime_number))
    else:
        print("{0}不是素数".format(prime_number))


Prime_Number(17)

# - 统计一个文本中每个单词出现个数
with open('./test3.txt', 'r') as f:
    str1 = f.read().split(' ')
    dict12 = collections.Counter(str1)
    for i in list(set(str1)):
        print("{0}的出现的次数是{1}次".format(i, dict(dict12)[i]))

import csv

# - 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
"""list_sum=[]
with open('test3.csv', 'r',encoding='gbk') as f:
    reader = csv.reader(f)
    for i in reader:
        list_sum.append(i)
with open('test2.csv', 'r',encoding='gbk') as f:
    reader = csv.reader(f)
    for i in reader:
        list_sum.append(i)
for a in range(len(list_sum//2)):
    if list_sum[a] != list_sum[a+len(list_sum//2)]:
        print()

"""
