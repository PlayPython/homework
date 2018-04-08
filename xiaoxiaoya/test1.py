#使用循环和算数运算，生成0到20的偶数
for i in range (0,21):
    if i%2 == 0:
        print(i)

#使用循环和算数运算，生成0到20的奇数
for i in range (0,21):
    if i%2 == 1:
        print(i)

#写一个函数，判断一个数能否被另外一个数整除
b = int(input("请输入b="))
def func(a):
    if a%b == 0:
        print("可以被整除")
    else:
        print("不可以被整除")
func(6)

# 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N
# <= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N（1<=N<=100）个
#随机数出来，对它们排序，然后显示这个子集

#创建一个函数，除去字符串前面和后面的空格
def str(a):
    b = a.strip()
    print(b)
str("   string  ")

#输入一个字符串，判断是否为回文
s = input("请输入字符串s：")
a = reversed(list(s))
if list(s) == list(a):
    print("输入字符串为回文")
else:
    print("输入的字符串不为回文")

##给出一个整型值，能够返回该值的英文，例如输入89，返回eighty-nine，限定值在0~100
x = input("请输入一个0~100的数：")


##给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数