'''author yanzi'''
#数值类型练习
#- 使用循环和算数运算，生成0到20的偶数
#- 使用循环和算数运算，生成0到20的奇数

def fun(n):
    a=[]
    b=[]
    for i in range(n+1):
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    #return(a,b)
    print("0到20偶数是{0}".format(a))
    print("0到20奇数是{0}".format(b))

fun(20)

#- 写一个函数，判断一个数是否被另外一个数整除
def sub(m,n):
    if m%n==0:
         print("{0}能被{1}整除".format(m,n))
    else:
         print("{0}不能被{1}整除".format(m,n))


sub(2,3)
sub(40,5)

#- 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N
#<= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N（1<=N<=100）个
#随机数出来，对它们排序，然后显示这个子集。

import random



#字符串和列
#- 创建一个函数，除去字符串前面和后面的空格
def drop(n):
    print("去掉前后空格的字符串为：{0}".format(n.strip()))

drop("#  asdggd  ")
drop("  sda ddgg ")


#- 输入一个字符串，判断是否为回文
def fun1(n):
    num=0
    for i in range(len(n)//2+1):#采用整除取值，避免了对于元素位数的奇偶判断
        if n[i]!=n[-1-i]: #理解回文字符串就是正向和反向排序都是一样的。
            num=num+1  #通过计数的方式，当相应位置对应相等时计数1次
    if num==0:
        print("{0}是一个回文字符串".format(n))
    else:
        print("{0}不是一个回文字符串".format(n))

fun1("abccba")
fun1("dvdv")

#- 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100


#- 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数






#字典和集合练习
#- 创建一个字典，把字典中的键按照字母顺序显示出来
#- 根据已经排序好的字母的键，显示这个字典中的键和值
#- 使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B





#文件和条件语句练习
#- 文件过滤，显示一个文件的所有行，忽略以#开始的行

#- 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号

#- 写一个函数，返回N的阶乘
def jiecheng(n):
    N=1  #1乘以任何数都为任何数本身，对结果没影响故赋了初始值1
    if isinstance(n,int) and n>=0: #阶乘是针对正整数而言的，规定0的阶乘为1，故多了一个判断
        for i in range(1,n+1):
            if n==0:
                N=1
            else:
                N=N*i #相当于依次乘到数本身
        print("{0}的阶乘是{1}".format(n,N))
        return(N)  #这个地方输出和返回的位置很重要
    else:
        print("{0}不存在阶乘".format(n))


jiecheng(4)
jiecheng(0)
jiecheng(-200)


#- 判断一个数字是否为素数
def sushu(n):
    num=0
    if isinstance(n,int) and n>1:#素数就是大于1的只能被1和它本身整除的整数，先做数据判断
        for i in range(1,n+1):
            if  n%i==0:
                num=num+1 #通过统计除数个数的方法来进行判断是否为素数
        if num>2:
            print("{0}不是一个素数".format(n))
        else:
            print("{0}是一个素数".format(n))
    else:
        print("{0}不是一个素数".format(n))

sushu(2)
sushu(1)
sushu(3.3)
#- 统计一个文本中每个单词出现个数


