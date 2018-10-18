#数值类型练习
#使用循环和算数运算，生成0到20的偶数
print([i for i in range(0, 21) if i % 2 == 0])
#使用循环和算数运算，生成0到20的奇数
print([j for j in range(0, 20) if j % 2 == 1])
#写一个函数，判断一个数是否被另外一个数整除
def a(x, y):
    if x % y == 0:
        print("%s能被%s整除" % (x, y))
        #print('(0)能被(1)整除'.formate(x,y))
    else:
        print('%s不能被%s整除' % (x, y))
a(3,7)
#判断一个数字是否为素数(质数)
def a(b):
    s = 0
    for a in range(1, b+1):
        if b % a == 0:
            s = s+1
    if s == 2:
        print('%d是素数' % b)
    else:
        print('%d不是素数' % b)
a(111)
#生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N <= 100）和（0<=n<=2**31 -1）。
#然后再随机从这个列表中取N（1<=N<=100）个 随机数出来，对它们排序，然后显示这个子集。

#字符串和列表
#创建一个函数，除去字符串前面和后面的空格
# hs = ' adf dfa   '
# b = hs.strip()
# print(b)
def hs(a):
    a = a.strip()
    print(a)
hs('     试试 函数   ')
#输入一个字符串，判断否为回文，如：'abccba''ada'
s = input('请输入一个字符串：')
if not s:
    print('请不要输入空字符串！')
    s = input('请重新输入一个字符串：')
a = len(s)
i = 0
count = 1
while i <= (a / 2):
    if s[i] == s[a - i - 1]:
        count = 1
        i += 1
    else:
        count = 0
        break
if count == 1:
    print('您所输入的字符串是回文')
else:
    print('您所输入的字符串不是回文')
#给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
#(前面20个数单独的，后面是组合)

#给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数

#字典和集合练习
#创建一个字典，把字典中的键按照字母顺序显示出来
a = {'z': 3, 'y': 4, 'b': 1, 'c': 2}
b = list(a.keys())
b.sort()
print(b)
#根据已经排序好的字母的键，显示这个字典中的键和值

#使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
import random
#定义一个函数用来生成满足题目要求的集合
def myFunc():
    '''生成一个满足特定要求的集合'''
    #定义一个空列表用来存储生成的随机数
    List = []
    #生成一个随机数，即确定要生成的集合的元素个数
    i = random.randint(1,10)
    for j in range(0,i+1):
        #产生０－９之间的随机数
        x = random.randint(0,9)
        #将生成的随机数添加到列表
        List.append(x)
    return set(List)
A = myFunc()
#打印集合Ａ
print(A)
B = myFunc()
#打印集合Ｂ
print(B)
print('*'*50)
#打印集合Ａ和Ｂ的交集
print(A&B)
#打印集合Ａ和Ｂ的并集
print(A|B)
#文件和条件语句练习
#文件过滤，显示一个文件的所有行，忽略以#开始的行

#比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
f1 = open("f:/test1.txt",'r')
f2 = open("f:/test2.txt",'r')
row = 0
for (line1, line2) in zip(f1, f2):
    row += 1
    if line1 == line2:
        pass
    else:
        col = 0
    print(row)
for (a, b) in zip(line1, line2):
    if a == b:
        col += 1
    else:
        print(col),
f1.close()
f2.close()
#统计一个文本中每个单词出现个数

#异常和错误练习
#使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断

#使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常

#函数练习
#定义一个函数，传入一个由数字组成列表，返回最大最小值
def hsh(a):
    print(max(a), min(a))
hsh([9,5,5,3,5,36,21,6567,663])
#定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数

#定义匿名函数，返回两数乘积

#写一个函数，返回N的阶乘
import math
def hsh(n):
    print(math.factorial(n))
hsh(6)
#把前面的一些练习题封装成一个个函数实现

#模块和类
#导入自定义模块里面的函数，并使用安装requests并使用，引入时候给requests包使用别名。
# 使用requests包调用github API获取返回值github API https://developer.github.com/v3/

#定义一个类，同时具有这样数据结构，实现四个方法

#unshift() 添加列表第一个元素

#push() 添加到列表最后一个元素

#pop() 返回并删除列表最后一个元素

#定义一个类，实现深度优先搜索和广度优先搜索两个方法

#定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承

#正则表达式
#匹配用空格分隔的任意一对单词，比如名和姓

#匹配以www.和.com结束的域名

#列出一个文件夹下所有文件的修改时间，获取文件的修改时间戳，比如HH:MM

#迭代器
#构造一个能够输出100以内的所有奇数的迭代器，打印里面的值

#用yield构造一个返回质数函数，从2开始，每次调用返回下一个更大的质数

#多线程
#尝试使用多线程方法访问github API并拿取数据，比如同时哪取20个用户的id信息
