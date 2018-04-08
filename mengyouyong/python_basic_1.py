import random
import math
import time

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

Comput_Date("2018-4-8","2018-4-3")

'''
#字典和集合练习
- 创建一个字典，把字典中的键按照字母顺序显示出来
- 根据已经排序好的字母的键，显示这个字典中的键和值
- 使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
'''
