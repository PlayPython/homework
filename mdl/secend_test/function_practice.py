# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 17:55
# @Author  : mdl
# @Email   : 1271737949@qq.com
# @File    : function_practice.py
# @Software: PyCharm

# - 定义一个函数，传入一个由数字组成列表，返回最大最小值
def max_min(array):
    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print("最大值为：", array[0])
    print("最小值为：",array[len(array)-1])

# max_min(array=[1,9,34,9999,78,100])

# - 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def para(*num,**dict):
    print("不定参数为：",num)
    print("字典参数为：",dict)
para(1,1,2,key=1,name="maomao")

# - 定义匿名函数，返回两数乘积

product=lambda a,b:a * b
sub=lambda a,b,c:a+b+c
# print ("两数乘积为：",product(5,2))
# print ("两数之和为：",sub(5,2,9))


# - 写一个函数，返回N的阶乘
def factorial(num):
    result=1
    for a in range(1,num+1):
        result=result*a
    print(num,"的阶乘数：",result)
# factorial(5)

# - 把前面的一些练习题封装成一个个函数实现