## 异常和错误练习
# - 使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
def try_except():

    try:
        with open('rsads', 'r') as f:
            print(f.readline())
    except Exception as e:
        print('the error message is: {0}'.format(e))
    finally:
        print('我一直都在')

try_except()
# - 使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常
def raise_input():
    b=input('please input positive integer')
    if b.isdigit():
        print('{0} is positive integer'.format(b))
    else:
        raise Exception('{0} is not positive integer'.format(b))

#raise_input()
# # 函数练习
# - 定义一个函数，传入一个由数字组成列表，返回最大最小值
def list_return_max_min(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)-1):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
    list_max=list[0]
    list_min=list[-1]
    print(list)
    print('最大值为{0},最小值为{1}'.format(list_max,list_min))

a=[5,6,10,18,3,1,8]
list_return_max_min(a)
# - 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def para(*args,**kwargs):
    print('不定参数是{0}，字典参数是{1}'.format(args,kwargs))

b={'a':'1','b':'2'}
c=["a","b","c"]
para(*c,**b)
# - 定义匿名函数，返回两数乘积
product=lambda x,y:x*y
print(product(3,2))


# - 写一个函数，返回N的阶乘
def factorial(x):
    num=1
    for i in range(1,x+1):
        num=num*i
    print(num)

factorial(5)
# - 把前面的一些练习题封装成一个个函数实现
#
# # 模块和类
# - 导入自定义模块里面的函数，并使用
# - 安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
#   + github API https://developer.github.com/v3/
# - 定义一个类，同时具有堆栈的数据结构，实现四个方法
#   + shift() 返回并删除列表最后一个元素
#   + unshift() 添加列表第一个元素
#   + push() 添加到列表最后一个元素
#   + pop()  返回并删除列表最后一个元素
# - 定义一个类，实现深度优先搜索和广度优先搜索两个方法
# - 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承