# 取0到20范围内的基数
# list_a = [i for i in range(0, 21) if i % 2]
# print(list_a)
# 取偶数
# list_b = [ i for i in range(0, 21) if (i % 2) - 1]
# print(list_b)

# 写一个函数判断一个数是否被另一个数整除
# def func(a, b):
#     if a % b == 0:
#         print("%d能被%d整除" % (a, b))
# func(4, 1)

# 判断一个数是否为素数
# def num(*a):
#     a = int(input("输入一个数："))
#     b = 0
#     for i in range(1, a + 1):
#         if (a % i) == 0:
#             b = b + 1
#     if b == 2:
#         print("该数是素数")
#     else:
#         print("该数不是素数")
# num()

# 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N <= 100）和（0<=n<=2**31 -1）。
# 然后再随机从这个列表中取N（1<=N<=100）个 随机数出来，对它们排序，然后显示这个子集。
# import random
# l1 = []
# l2 = []
# b = random.randrange(2, 101)
# for i in range(b):
#     l1.append(random.randrange(2**31 - 1))
# print(b)
# print(l1)
# n = random.randrange(2, 101)
# for i in range(n):
#     l2.append(l1[random.randrange(b)])
# l2.sort()
# print(n)
# print(l2)

# 创建一个函数，除去字符串前面和后面的空格

# def func(a):
#     print(a.strip())
#
#
# func(" str i n g   ")

# 输入一个字符串，判断是否为回文
# def func(*a):
#     a = str(input("输入一个字符串："))
#     if len(a) % 2 == 0:
#         b = int(len(a) / 2)
#         c = 0
#         for i in range(b):
#             if a[i] == a[-(i+1)]:
#                 c += 1
#         if c == b:
#             print("%s是回文"%a)
#         else:
#             print("%s不是回文"%a)
#     else:
#         print("%s不是回文"%a)
#
# func()


# 给出一个整型值，能够返回该值的英文，例如输入89，返回eighty-nine，限定值在0~100


# def func(*a):
#     a = int(input("请输入0-100的整数："))
#     l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     l2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#     l3 = [20, 30, 40, 50, 60, 70, 80, 90]
#     l4 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     l5 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
#     l6 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#     list_1 = dict(zip(l1, l4))
#     list_2 = dict(zip(l2, l5))
#     list_3 = dict(zip(l3, l6))
#
#     print(a)
#     print(list_1)
#     print(list_2)
#     print(list_3)
#
#
# func()
# 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数

# num = 1
#
#
# def fun1():
#     global num
#     print(num)
#     num = 123
#     print(num)
#
#
# fun1()
# print(num)

# a = 10
#
#
# def test(a):
#     a = a + 1
#     print(a)
#
#
# test(a)
# 使用try-except处理文件打开异常，打开一个不存在的文件，
# 打印提示信息，但是程序不中断
# try:
#     with open("file.txt", "r") as f:
#         print(f.readlines())
# except FileNotFoundError as ne:
#     print(ne)
# print("程序继续执行")
#

# 使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，
# 强制抛出异常

# def func(*n):
#     n = int(input("只能输入正整数:"))
#     try:
#         print(n)
#     except Exception as e:
#         raise e
#
#
# func()
# print("程序继续")

# 定义一个函数，传入一个由数字组成列表，返回最大最小值
# def extreme_value(*args):
#     print(max(args))
#     print(min(args))
#
#
# a = [10, 20, 30, 55, 66]
#
# extreme_value(*a)

# 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# a = (1, 2, 3)
# b = {"name": "BOb", "age": 25}
# func(*a, **b)

# 定义匿名函数，返回两数乘积
# f = lambda x, y: x * y
# print(f(2, 3))

# 写一个函数，返回N的阶乘
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
#
# print(fact(10))

# 导入自定义模块里面的函数，并使用
# from Moduel_B import add
#
# c = add(2, 3)
# print(c)

# 安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
# github API https://developer.github.com/v3/
# import requests as RQ
#
# r = RQ.get("https://developer.github.com/v3/")
# print(r.text)

# 定义一个类，同时具有这样数据结构，实现三个方法
# unshift() 添加列表第一个元素
# push() 添加到列表最后一个元素
# pop() 返回并删除列表最后一个元素


# 定义一个类，实现深度优先搜索和广度优先搜索两个方法
# 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
# 更新示例中car的display_car方法，使其通用性更强，比如打印每个参数，而不只是父类的几个参数
