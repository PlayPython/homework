import random

# 数值类型练习
# 使用循环和算数运算，生成0到20的偶数
# # print([i for i in range(21) if i % 2 == 0])
# 使用循环和算数运算，生成0到20的奇数
# # print(list(i for i in range(21) if i % 2 != 0))
# 写一个函数，判断一个数是否被另外一个数整除
# 判断一个数字是否为素数


# def zc(a, b):
#     if a % b == 0  :
#         print('{0}能够被{1}整除'.format(a, b))
#     else:
#         print('%s不能被%s整除' % (a, b))
# zc(10,2)
#
# def zc(num):
#     s = 0
#     for i in range(1,num+1):
#         if num % i ==0 :
#             s+=1
#     if s == 2:
#         print('%d是素数' % num)
#     else:
#         print('%d不是素数' % num)
# zc(9)

# 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N <= 100）和（0<=n<=2**31 -1）。
# 然后再随机从这个列表中取N（1<=N<=100）个 随机数出来，对它们排序，然后显示这个子集。

# def sjs():
#     li=[]
#     d = []
#     s=0
#     for i in range(random.randint(2,101)):
#         li.append(random.randint(0,2**31-1))
#         s+=1
#     print(li)
#     for j in range(random.randrange(1,101)):
#         a = random.randint(0,s-1)
#         d.append(li[a])
#         li.pop(a)
#         s = s-1
#         d.sort()
#     print(d)
# sjs()

# 字符串和列表
# 创建一个函数，除去字符串前面和后面的空格
# def kg(value):
#     print(value.strip(' '))
# kg('  sfsd    ')
# 输入一个字符串，判断是否为回文
# def hw(value):
#     s = 0
#     for i in range(len(value)//2):
#         if value[i] == value[-(i+1)]:
#             s+=1
#     if s == len(value)/2 or s == (len(value)-1)/2:
#         print('%s是回文' % value)
#     else:
#         print('%s不是回文' % value)
# hw('12321')
# hw('1221')
# 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
# def zh(value):
#     fy={"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
#     b = ''
#     value = str(value)
#     for i in range(len(value)):
#         a = fy[(value[i])]
#         b = b + a + '-'
#         c = b.rstrip('-')
#     print(c)
# zh(97)
# 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
# def days(date1,date2):






# 字典和集合练习
# # 创建一个字典，把字典中的键按照字母顺序显示出来
# dic = {"c":1, "a":2, "d":3, "b":4}
# a=list(dic.keys())
# a.sort()
# print(a)
#  根据已经排序好的字母的键，显示这个字典中的键和值
# dic = {"c":1, "a":2, "d":3, "b":4}
# a=list(dic.keys())
# a.sort()
# print(a)
# for i in a:
#     print(dic[i],end='\t')


# 使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
# def jh():
#     li=[]
#     d = []
#     for i in range(random.randint(0,9)):
#         li.append(random.randint(0,9))
#         d.append(random.randint(0, 9))
#     a = set(li)
#     b = set(d)
#     print(a,b)
#     print(a|b,a&b)
# jh()

# 文件和条件语句练习
# 文件过滤，显示一个文件的所有行，忽略以#开始的行

# 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号

# 统计一个文本中每个单词出现个数
# 定义一个函数，传入一个由数字组成列表，返回最大最小值
# def dx(value):
#     print(max(value),min(value))
# dx([1,5,6,3])
# # 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
# def dy(*a,**b):
#     print(a,b)
# dy([456,2],{"a":1,"b":2})

# 定义匿名函数，返回两数乘积
# c = lambda a, b : a * b
# a = 3
# b = 4
# print (c(a,b))

# 写一个函数，返回N的阶乘
# import math
# def jc(num):
#     print(math.factorial(num))
# jc(3)


# 异常和错误练习
# 使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
# try:
#     f = open('rept.html','r')
#     f.close()
# except:
#     print('文件不存在')
# 使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常

a = input('')
if int(a):
    raise Exception('只能输入正整数')
    print(a)
print(a+'test')


