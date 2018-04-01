#使用循环和算数运算，生成0到20的偶数
def even_number():
    l=range(20)
    for i in l:
        if i%2==0:
            print("0到20的偶数为:",i)
even_number()
#使用循环和算数运算，生成0到20的奇数
def Odd_number():
    o=range(20)
    for i in o:
        if i%2!=0:
            print("0到20的奇数为：",i)
Odd_number()
#写一个函数，判断一个数是否被另外一个函数整除
def divisible(a,b):
    if a%b==0:
        print(a,"能被" ,b ,"整除")
    else:
        print(a, "不能被", b, "整除")
