#异常和错误练习
#使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断

def tryy(a):
    try:
        open(a,"r")
    except IOError:
        print("读取文件失败")

tryy("D:/a.txt")
#使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常

def integer(a):
    if type(a)!=int or a<=0:
        raise ValueError("输入不为正整数")

integer("aaa")

#函数练习
#定义一个函数，传入一个由数字组成列表，返回最大最小值
def mun_list(mun=[1,2,3,4]):
    return max(mun),min(mun)

mun_list()
#定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def function_1(*mun1,**mun2):
    print(mun1,mun2)

function_1([1,2,3,4],{"a":1,"b":2},a=1,b=2)

#定义匿名函数，返回两数乘积
mul=lambda x,y:x*y
print(mul(3,4))
#写一个函数，返回N的阶乘
def factorial(N):
    fac=1
    for i in range(1,N+1):
        fac=fac*i
    return fac

factorial(5)

#把前面的一些练习题封装成一个个函数实现




