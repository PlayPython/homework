#数值类型练习

#1、使用循环和算数运算，生成0到20的偶数

def os_print():
    for i in range(0,21):
        if i%2==0:
            print(i)

if __name__ == '__main__':
 os_print()

#2、使用循环和算数运算，生成0到20的奇数
def js_print():
    for i in range(0,21):
        if i%2!=0:
            print(i)

if __name__ == '__main__':
 js_print()

#3、写一个函数，判断一个数是否被另外一个函数整除
def js_print(a,b):
    a = int(input("输入一个数："))
    b = int(input("输入一个数："))
    if b == 0:
        print("b不能输入0")
    if a % b == 0:
        print("能整除")
    else:
        print("不能整除")
if __name__ == '__main__':
 js_print(3,3)




#4、生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N <= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N（1<=N<=100）个 随机数出来，对它们排序，然后显示这个子集。





#字符串和列表

#5、创建一个函数，除去字符串前面和后面的空格
def kg_print():
    k=" 字符串  "
#删除两端的空格
    print(k.strip())
#删除右边空格
    print(k.rstrip())
#删除左边空格
    print(k.lstrip())

if __name__ == '__main__':
 kg_print()


#6、输入一个字符串，判断是否为回文
def hw_print():
    h = input("请输入字符串：")
    j=reversed(list(h))
    if list(h)==list(j):
        print("你输入的字符串是回文")
    else:
        print("不是回文")
if __name__ == '__main__':
 hw_print()
#采用reversed()函数前，将字符串转化成字符串列表；2，reversed(seq)函数返回的是一个迭代器，将其显示出来，需要list(reversed(seq))。

#7、给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100







#8、给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
import time
import datetime
def kg_print(rq,rq2):
    #rq = input("请输入字符串：")
    #rq2 = input("请输入字符串：")
    gs1 = time.strptime(rq, "%m/%d/%Y")
    zgs = time.strftime("%Y%m%d", gs1)
    gs2 = time.strptime(rq2,  "%d/%m/%Y")
    zgs1 = time.strftime("%Y%m%d", gs2)
    a1 = datetime.datetime.strptime(zgs, "%Y%m%d")
    a2 = datetime.datetime.strptime(zgs1, "%Y%m%d")
    dys = (a2 - a1).days
    print("相隔天数", dys)
if __name__ == '__main__':
 kg_print("3/2/2018","8/3/2018")


#字典和集合练习

#9、创建一个字典，把字典中的键按照字母顺序显示出来，比如"ABCBA"是一个回文

#10、根据已经排序好的字母的键，显示这个字典中的键和值

#11、使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B



#文件和条件语句练习

#12、文件过滤，显示一个文件的所有行，忽略以#开始的行
def fg():
    wf3 = open("D:/f3.txt")
    for eachLine in wf3:
        if eachLine[0] != '#':
            print("行",eachLine)
if __name__ == '__main__':
    fg()



#13、比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号


def bj_print():
    wf1 = open("D:/f1.txt")
    wf2 = open("D:/f2.txt")
    h = 0  # 记录出现不同字符的行
    for (l1, l2) in zip(wf1, wf2):
        h += 1
        if l1 == l2:
            pass
        else:
            col = 0;
            print(h)
              # 记录不同字符出现的列号
            for (a1, b1) in zip(l1, l2):
                if a1 == b1:
                    col += 1
                else:
                    print(col)
    wf1.close()
    wf2.close()

if __name__ == '__main__':
 bj_print()







#14、写一个函数，返回N的阶乘

def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)


su = int(input("请输入一个正整数:"))
result = jc(su)
print("%d 的阶乘是 %d" % (su, result))
if __name__ == '__main__':
    jc(6)



#15、判断一个数字是否为素数

def ss_print():
    n1=int(input("请输入一个数："))
    for i in range(2,n1):
        if n1%i==0:
            print("不是素数")
            break
    else:
        print("是素数")

if __name__ == '__main__':
 ss_print()

#16、统计一个文本中每个单词出现个数

def tj_print():
    n2="world is happy happy"
       #字符串分割成单词列表
    list1=n2.split()
    #去重
    set1=set(list1)
    #集合转列表
    list2=list(set1)

    #新建字典
    dir1={}
    for k in range(len(list2)):
        dir1[list2[k]] = 0
        for y in range(len(list1)):
            if list2[k] == list1[y]:
                dir1[list2[k]] += 1
    print(dir1)

if __name__ == '__main__':
 tj_print()
