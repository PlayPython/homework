#使用循环和算数运算，生成0到20的偶数
for i in range(21):
    if i % 2 == 0:
        print(i)

#使用循环和算数运算，生成0到20的奇数
for i in range(21):
    if i % 2 != 0:
        print(i)

#写一个函数，判断一个数是否被另外一个函数整除
def func(i,j):
    if i % j == 0:
         print("%s可以被%s整除" % (i,j))
    else:
         print("%s不可以被%s整除" % (i,j))
func(4,2)

#判断一个数字是否为素数(质数)
def zs (a): 
    m=[] 
    for i in range(1,a):
        if a%i==0: 
           m.append(a) 
    if len(m)<2: 
        print("%s是素数" % a) 
   else: 
       print("%s不是素数" % a)
       
zs(13)


# 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N <= 100）和（0<=n<=2**31 -1）。
# 然后再随机从这个列表中取N（1<=N<=100）个 随机数出来，对它们排序，然后显示这个子集
#
# 创建一个函数，除去字符串前面和后面的空格
def str1(a):
    print(str.strip(a))
str1("          sdds ")

#输入一个字符串，判断是否为回文

def str2(a):
    for i in range((len(a)//2)+1):
        if a[i] != a[-(i + 1)]:
            print("%s不是回文" % (a))
            break
    else:
        print("%s是回文" % (a))
str2("12345321")

#给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100


#给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数


#创建一个字典，把字典中的键按照字母顺序显示出来
a = {"y": 2, "x": 1, "z": 3, "m" : 5,"l" : 0 }
b = list(a.keys())
b.sort()
print(b)

#根据已经排序好的字母的键，显示这个字典中的键和值

#使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
import random
def set1():
    A = set()
    B = set()
    for i in range(10):
        A.add(random.randint(10))
        B.add(random.randint(10))
    print(A,B)
    print(A|B,A&B)

set1()

# A = set()
# B = set()
# for i in range(10):
#     A.add(random.randint(10))
#     B.add(random.randint(10))
# print(A,B)
# print(A|B,A&B)

# 文件过滤，显示一个文件的所有行，忽略以#开始的行
f = open("test","r")
with open ("test","r") as f:
    print(f.readlines())

# 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号

# 统计一个文本中每个单词出现个数






