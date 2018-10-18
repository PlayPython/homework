# 使用循环和算数运算，生成0到20的偶数
print ([i for i in range(21) if i % 2 == 0])

# 使用循环和算数运算，生成0到20的奇数
print ([i for i in range(21) if i % 2 != 0])

# 写一个函数，判断一个数是否被另外一个数整除
def zc(a,b) :
    if a%b==0:
        print ("%s能被%s整数" % (a,b))
    else :
        print ("%s不能被%s整数" % (a,b))
zc(2,2)
zc(1,2)


# 判断一个数字是否为素数
def ss (a):
    li=[]
    for i in range(1,a):
        if a%i==0:
            li.append(a)
    if len(li)<2:
        print("%s是素数" % a)
    else:
        print("%s不是素数" % a)


ss(13)

# 生成一个有N个元素的由随机数n组成的列表，
# 其中N和n的取值范围分别为（1< N <= 100）
# 和（0<=n<=2**31 -1）。然后再随机从这个列表中
# 取N（1<=N<=100）个 随机数出来，对它们排序，然后显示这个子集。
import random
li=[]
li1=[]
N=random.randint(2,100)
# N1=random.randint(1,100)

for i in range(N+1):
    n=random.randint(0,2**31-1)
    li.append(n)
for j in range(N+1):
    li1.append(li[j])
print(li1)

# 字符串和列表
# 创建一个函数，除去字符串前面和后面的空格
def qkg(a):
    a=a.strip()
    print(a)

qkg('   123     ')

# 输入一个字符串，判断是否为回文
# def hw(a):
#     a=a.split("")
#     a=list(a)
#
#     if a==reversed(a):
#
#         print("2222221")
def hw(a):
    li=[]
    for i in range(len(a)//2):
        if a[i]==a[-(i+1)]:
            li.append(i)
    if len(li)==len(a)//2:
        print("%s是回文"% a)
    else:
        print("%s不是回文" % a)

hw("你好你")
hw("你好好你")


# 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
def fy(a):
    pass








# 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数





# 字典和集合练习
# 创建一个字典，把字典中的键按照字母顺序显示出来
a={'for':4,'one':1,'two':2,'three':3,'a':2}
b=sorted(a.keys())
print(b)


# 根据已经排序好的字母的键，显示这个字典中的键和值
li=[]
for i in range(len(b)):
    li.append(a[b[i]])
c=dict(zip(b,li))
print(c)

# 使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A | B和A & B
li=[]
for i in range(random.randint(0,10)):
    for j in range(random.randint(0,10)):
        li.append(j)

li1=[]
for i in range(random.randint(0,10)):
    for j in range(random.randint(0,10)):
        li1.append(j)
a=set(li)
b=set(li1)

print('a=%s'%a)
print('b=%s'%b)
print('a|b=%s'%(a|b))
print('a&b=%s'%(a&b))


# 文件和条件语句练习
# 文件过滤，显示一个文件的所有行，忽略以  # 开始的行
# 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
# 统计一个文本中每个单词出现个数
# 异常和错误练习
# 使用try - except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
# 使用raise强制抛出异常，input()
# 只接受正整数的输入, 否则中断程序，强制抛出异常
# 函数练习
# 定义一个函数，传入一个由数字组成列表，返回最大最小值
# 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
# 定义匿名函数，返回两数乘积
# 写一个函数，返回N的阶乘
# 把前面的一些练习题封装成一个个函数实现
# 模块和类
# 导入自定义模块里面的函数，并使用
# 安装requests并使用，引入时候给requests包使用别名。使用requests包调用github
# API获取返回值
# github
# API
# https: // developer.github.com / v3 /
# 定义一个类，同时具有这样数据结构，实现四个方法
# unshift()
# 添加列表第一个元素
# push()
# 添加到列表最后一个元素
# pop()
# 返回并删除列表最后一个元素
# 定义一个类，实现深度优先搜索和广度优先搜索两个方法
# 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
# 正则表达式
# 匹配用空格分隔的任意一对单词，比如名和姓
# 匹配以www.和.com结束的域名
# 列出一个文件夹下所有文件的修改时间，获取文件的修改时间戳，比如HH: MM
# 迭代器
# 构造一个能够输出100以内的所有奇数的迭代器，打印里面的值
# 用yield构造一个返回质数函数，从2开始，每次调用返回下一个更大的质数
# 多线程
# 尝试使用多线程方法访问github
# API并拿取数据，比如同时哪取20个用户的id信息