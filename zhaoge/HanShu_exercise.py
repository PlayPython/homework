# 异常和错误练习
import math
#使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常
def input_f():
    x=input('请输入正整数')
    #if type(x)!=type(1):
    if isinstance(x,int):
        raise NameError('您输入的不是整数')
    elif int(x)<=0:
        #raise NameError('您输入的不是正数')
        raise Exception('您输入的不是正数')
    else:
        print('输入正确')


#使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
def open_f():
    try:
        file=open('123.txt')
    except FileNotFoundError as e:
        print(e)
        print('文件不存在，朋友')

# 函数练习
#定义一个函数，传入一个由数字组成列表，返回最大最小值
def max_min():
    l=input('传入一个由数字组成列表')
    ll=l.split(',')#分隔开后，还是字符串组成的列表
    a=max(ll)
    b=min(ll)
    #print('最大值是{0},最小值是{1}'.format (max(ll),min(ll)))
    print('最大值是%s,最小值是%s' % (a,b))

def mn():
    l = input('传入一个由数字组成列表')
    print('最大值是{0},最小值是{1}'.format(max(l), min(l)))
#结果：
#传入一个由数字组成列表1,2,3
#最大值是3,最小值是,
#解析：因为字符串最小值，就是，

#定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def kebian_f(m,n=[],*a,**b):
    print(a)

#定义匿名函数，返回两数乘积
cheng=lambda x,y:x*y

#阶乘-----自带阶乘函数
def jiecheng(a):
    print(math.factorial(a))

#阶乘
def jc(m):
    n=1#函数中定义就行
    for i in range(1,m+1):
        n=n*i
    print(n)

def jcc(m,n=1):

    for i in range(1,m+1):
        n=n*i
    print(n)#用的时候，jcc(3)，jcc(3，1)，jcc(3，n=1)都行

# 模块和类

#安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
#github API https://developer.github.com/v3/
#安装requests------pip install requests
import requests as re
def get_api():
    response=re.get('https://developer.github.com/v3/')
    print(response.text)#这里必须用.text,不然打印不出来

def get_baidu():
    response=re.get('http://www.baidu.com')
    print(response.content)

def post_f():

    response=re.post('http://192.168.1.241:8080/login',{'name':'jack','password':'123456'})
    print(response.content)

# 定义一个类，同时具有这样数据结构，实现四个方法
# unshift() 添加列表第一个元素
# push() 添加到列表最后一个元素
# pop() 返回并删除列表最后一个元素
class list_f():
    #def __init__(self,l):
         #self.l=l

    def unshift_f(self,a,*l):
        ll=list(l)
        ll.insert(0,a)
        print(ll)


    def push_f(self,lastone,*l):
        ll = list(l)
        ll.append(lastone)
        print(ll)

    def pop_f(self,*l):
        ll = list(l)
        print(ll[-1])
        del ll[-1]

        print(ll)


class list_ff():
    #这一步就是为了后面不用每次都传list，这里传了*l,后面就不用写了，可和list_f相比
    def __init__(self,*l):
        self.l=l

    def unshift_f(self, a):
        ll = list(self.l)#这里要用self.l,用l不行要报错。
        ll.insert(0, a)
        print(ll)

    def push_f(self, lastone):
        ll = list(self.l)
        ll.append(lastone)
        print(ll)

    def pop_f(self):
        ll = list(self.l)
        print(ll[-1])
        del ll[-1]

        print(ll)

#定义一个类，实现深度优先搜索和广度优先搜索两个方法

# 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
class Pet():
    def __init__(self,name):
        self.name=name
    def run(self):
        print('run run run')
    def eat(self):
        print('eat eayt eat')

class Cat(Pet):
    def cat(self):
        print('the best friend of mouse')

class Dog(Pet):
    def dog(self):
        print('like eating poo poo')








if __name__ == "__main__":
    open_f()
    input_f()
    max_min()
    kebian_f(1,[],(1,2,3,4,5),a="a1",a1="a1")#字典需要这样写，不然打印出来就把前面的tuple也连在一起了
    #kebian_f(1,(1,2,3,4,5))#有问题，打印出来是个空括号。
    kebian_f(1,[], (1, 2, 3, 4, 5))#这样可以正确打印tuple
    kebian_f(1, a="a1",a1="a1")#这样可以正确打印dic
    kebian_f(1,[], a="a1", a1="a1")  # 这样可以正确打印dic
    print(cheng(2, 3))#匿名函数
    jiecheng(3)
    jc(3)
    jcc(3)
    l=list_f()#实例化一个类的时候，类名后面要加（）
    tu=('a','b')
    l.push_f('0','a','b')
    l.pop_f('a','b')
    l=list_ff('a','b')
    l.unshift_f('first')
    orange_cat = Cat('oc')
    orange_cat.eat()
    orange_cat.cat()


