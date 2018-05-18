#name：qiuqiu  chenqiumin
#数值类型练习
# 使用循环和算数运算，生成0到20的偶数
for i in range(0,21,2):
	print("0到20的偶数为:",i)

# 使用循环和算数运算，生成0到20的奇数
for i in range(1,20):
    if i%2!=0:
        print("0到20的奇数为：",i)

# 写一个函数，判断一个数是否被另外一个数整除
def divisible(a,b):
    if a>=b:
        if a%b==0:
            print(a,"能被" ,b ,"整除")
        else:
            print(a, "不能被", b, "整除")
    else:
        if b%a==0:
            print(b,"能被" ,a ,"整除")
        else:
            print(b, "不能被", a, "整除")
# 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N
#<= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N（1<=N<=100）个
#随机数出来，对它们排序，然后显示这个子集。
import random
def random_list():
    list = []
    N = random.randint(1, 101)
    for item in range(N):
        nn = random.randint(0, 2 ** 31 - 1)
        list.append(nn)
    print(list)
    list.sort()
#字符串和列表
#创建一个函数，除去字符串前面和后面的空格
def trim(s):
    length = len(s)
    if length > 0:
        for i in range(length):
            if s[i] != ' ':
                break;
        j = length-1;
        while s[j] == ' ' and j >= i:
            j -= 1
        s = s[i:j+1]
    return s