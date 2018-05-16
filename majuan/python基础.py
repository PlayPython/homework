#异常和错误练习
# #使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
try:
    file=open("A.txt")
    file.close()
except FileNotFoundError:
    print("文件不存在！")
finally:
    print('程序不中断')

#使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常


def zzs():
    a=input()
    if type(a)==type(1):
        print(a)
    else:
        raise ValueError('输入类型不合法')
zzs()


#函数练习
#定义一个函数，传入一个由数字组成列表，返回最大最小值

def dxz(a):
    return max(a),min(a)
li=dxz([1,2,3,4,5])
print(li)

#定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数

def get_args(*args):
    print(args)
get_args(3,'ji','jj,ff',88)
get_args({
        'a':1,
        'b':2,
        'c':3,
        'd':'hello'
    })

#定义匿名函数，返回两数乘积

f = lambda a,b:a*b
print(f(2,3))


#写一个函数，返回N的阶乘
def jc(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
print(jc(4))

#把前面的一些练习题封装成一个个函数实现

#模块和类

#导入自定义模块里面的函数，并使用
#见同目录下的“引入”文件

#安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
#github API https://developer.github.com/v3/

#定义一个类，同时具有这样数据结构，实现四个方法
#unshift() 添加列表第一个元素
#push() 添加到列表最后一个元素
#pop() 返回并删除列表最后一个元素
#定义一个类，实现深度优先搜索和广度优先搜索两个方法

#定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
class Pet():
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
    def eat(self):
        print('%s吃饭了'%(self.name))

# a=Pet('虫虫','男',3)
# a.eat()

class Cat(Pet):
    def sleep(self):
        print('%s今年%d岁了'%(self.name,self.age))
b=Cat('小虫','女',2)
b.eat()
b.sleep()

class Dog(Pet):
    def play(self):
        print('%s性别是%s,%d岁'%(self.name,self.sex,self.age))
c=Dog('小小虫','男',1)
c.eat()
c.play()

