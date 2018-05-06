# 数值类型练习
# 使用循环和算数运算，生成0到20的偶数
'''
def evennumber():
    for i in range(0, 21):
        if i % 2 == 0:
            print("生成的偶数为：", i)


evennumber()
'''

# 使用循环和算数运算，生成0到20的奇数
'''
def oddnumber():
    for i in range(0, 21, ):
        if i % 2 == 1:
            print("生成的偶数为：", i)


oddnumber()
'''

# 写一个函数，判断一个数是否被另外一个数整除
'''
def fun(number, num):
    if number % num == 0:
        print(number, '能整除', num)
    else:
        print(number, '不能整除', num)


fun(5, 5)
'''
# 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为
# （1 <N <= 100）和（0 <= n <= 2 ** 31 -1）。
# 然后再随机从这个列表中取N（1 <= N <= 100）个随机数出来，对它们排序，然后显示这个子集。
'''
import random

def Random():
    list = []
    Num = []
    N = random.randint(2, 100)
    for i in range(N):
        n = random.randint(0, 2 ** 31 - 1)
        list.append(n)
        list.sort()
    print(list)


Random()
'''
# 字符串和列表
# 创建一个函数，除去字符串前面和后面的空格
'''
def Except():
    str = "  除去字符串前面和后面的空格  "
    Str = str.strip()
    print(Str)


Except()
'''


# 输入一个字符串，判断是否为回文
'''
def String(string):
    s = 0
    if len(string) % 2 != 0 and len(string) > 2:
        for i in range(len(string) // 2):
            j = -(i + 1)
            if string[i] == string[j]:
                s = s + 1
                if s == len(string) // 2:
                    print('是回文')
            else:
                print('不是回文')
                break
    else:
        print('不是回文')


String('12321')
'''
# 给出一个整型值，能够返回该值得英文，例如输入89，返回八九，限定值在0〜100


# 给出两个可以识别格式的日期，比如MM / DD / YY或者DD / MM / YY计算两个日期的相隔天数


# 字典和集合练习
# 创建一个字典，把字典中的键按照字母顺序显示出来

# 根据已经排序好的字母的键，显示这个字典中的键和值

# 使用随机数模块生成一个随机数集合甲和B，每个集合是0到9的随机数集合生成之后显示结果A |。乙和A＆B


# 文件和条件语句练习
# 文件过滤，显示一个文件的所有行，忽略以＃开始的行

# 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号

# 写一个函数，返回Ñ的阶乘

# 判断一个数字是否为素数

# 统计一个文本中每个单词出现个数
