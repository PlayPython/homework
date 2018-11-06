#!/usr/bin/python
# # -*- coding:utf-8 -*-






#定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def func (*tup,**dict):
        print (tup)
        print (dict)


func(1,2,3)
func(*[1,2,3])
func(a=4,b=5,c=6)
func(1,2,3,a=4,b=5,c=6)



#定义匿名函数，返回两数乘积
# true方法等价于匿名函数表达式
true = lambda: True
print(true())


def add(x, y):
    return x * y


print(add(1, 2))

add = lambda x, y: x * y
print(add(1, 2))










