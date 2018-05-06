# 异常和错误练习
# 使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
def try_except_open():
    try:
        f = open("huang", "r")
    except FileNotFoundError as a:
        print(a)
        print("打开的文件不存在")


try_except_open()


# 使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常
def raise_input():
    num = int(input("请输入正整数："))
    if num > 0:
        print(num)
    else:
        raise Exception("你输入的不是正整数")


raise_input()
# 函数练习
# 定义一个函数，传入一个由数字组成列表，返回最大最小值



# 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
# 定义匿名函数，返回两数乘积
# 写一个函数，返回N的阶乘
# 把前面的一些练习题封装成一个个函数实现



# 模块和类
# 导入自定义模块里面的函数，并使用
# 安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
# github API https://developer.github.com/v3/
# 定义一个类，同时具有堆栈的数据结构，实现四个方法
# shift() 返回并删除列表最后一个元素
# unshift() 添加列表第一个元素
# push() 添加到列表最后一个元素
# pop() 返回并删除列表最后一个元素
# 定义一个类，实现深度优先搜索和广度优先搜索两个方法
# 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
