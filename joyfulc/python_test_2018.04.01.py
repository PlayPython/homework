
import random
import datetime

print("\n\n使用循环和算数运算，生成0到20的奇数:")
for x in range(1,21):
    if(x%2!=0):
        print(x,end=',')

print("\n\n使用循环和算数运算，生成0到20的偶数:")
for y in range(1,21):
    if(y%2==0):
        print(y,end=',')

#print("\n\n写一个函数，判断一个数是否被另外一个数整除:")
def my_func(my1,my2):
    if isinstance(s1, int) != True:
        print("你输入的是string，我现在要把你输入的string转换成int类型再使用")
        my3=int(my1)
        my4=int(my2)
    if my3%my4==0:
        print("{0}可以被{1}整出".format(my3,my4))
    else:
        print("{0}不可以被{1}整出".format(my3,my4))

print("\n\n生成一个有N个元素的由随机数n组成的列表,"
"\n其中N和n的取值范围分别为（1< N<= 100）和（0<=n<=2**31 -1）,"
"\n然后再随机从这个列表中取N（1<=N<=100）个随机数出来，对它们排序，然后显示这个子集:")
N=random.randint(2,101)
print("随机数N为：{0}".format(N))
randlist=random.sample(range(0,2**31),N)
randlist2=randlist[:]
randlist2.sort()
print("排序前的子集：{0},\n排序后的子集：{1}".format(randlist,randlist2))

#创建一个函数，除去字符串前面和后面的空格
def delspace(str1):
    str2=str1.strip()
    print("你输入的是：{0},我帮你处理后：{1}。".format(str1,str2))

#输入一个字符串，判断是否为回文
def huiwen(str3):
    str4=reversed(str3)
    if list(str4)==list(str3):
        print("恭喜，你输入的{0}是回文".format(str3))
    else:
        print("额，你输入的{0}不是回文".format(str3))

#给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
def mun_str(num1):
    dicnum1={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    dicnum2={20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
    if (num1>=0 and num1<20):
        print(dicnum1[num1])
    elif (num1>=20 and num1<100):
        num2=num1//10
        num3=num1%10
        print("{0}-{1}".format(dicnum2[num2*10],dicnum1[num3]))
    elif num1==100:
        print("one-hundred")
    else:
        print("太顽皮了，我现在只接受0-100的输入哦")

'''
#给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
#d1 = datetime.date(year1, month1, day1)
#d2 = datetime.date(year2, month2, day2)
#print((d1 - d2).days)
def count_day(str5,str6):
    str5=datetime.date(str5)
    str6=datetime.date(str6)
    print(str6-str5)
count_day('2018-03-04','2018-04-04')
'''

if __name__=="__main__":
    print("\n写一个函数，判断一个数是否被另外一个数整除:")
    s1 = input("请输入除数:")
    s2 = input("请输入被除数:")
    my_func(s1,s2)
    print("\n除去字符串前面和后面的空格:")
    s3 = input("请输入一个字符串，最好前后有空格:")
    delspace(s3)
    print("\n判断回文:")
    s4 = input("请随意输入一个字符串:")
    huiwen(s4)
    s5 = input("请随意输入一个0-100的数字:")
    mun_str(int(s5))










