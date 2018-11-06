#!/usr/bin/python
# # -*- coding:utf-8 -*-



#使用尝试 - 除了处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
# 捕获指定异常，并让程序继续进行
def catch_specific_exception():
    try:
        open("blala", 'r')
    except FileNotFoundError as e:
        print(e)  # 打印系统标准异常信息
        print("could not open the file")  # 打印自定义信息
    try:
        1 / 0
    except ZeroDivisionError as e:
        print("There is something wrong with Division,reason:{0}".format(e))
catch_specific_exception()


def wenjian_exception():
    try:
         open("aa",'r')
    except FileNotFoundError as e:
        print(e)   # 打印系统标准异常信息
        print("could not open the file")  # 打印自定义信息
wenjian_exception()



#使用提高强制抛出异常，输入（）只接受正整数的输入，否则中断程序，强制抛出异常
def raise_function1(input_para):
    if isinstance(input_para, int):
        print("input para".format(input_para))
    else:
        raise AssertionError("parameter type should be int, however it is {}".format(type(input_para)))

raise_function1('qwe')


def numble():
    a=[1,2,3,4]
    return max(a)


# lambda表达式返回可调用的函数对象
def true():
    return True


print(true())

#定义匿名函数，返回两数乘积
# true方法等价于匿名函数表达式
true = lambda: True
print(true())


def add(x, y):
    return x * y


print(add(1, 2))

add = lambda x, y: x * y
print(add(1, 2))







