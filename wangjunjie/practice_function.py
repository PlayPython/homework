'''
@author: wangjunjie
@contact: wangjunjie_93@163.com
@file: practice_function.py
@time: 2018\5\6 0006 17:50
@desc:函数练习
'''


# 定义一个函数，传入一个由数字组成列表，返回最大最小值
def functionList(numList):
    print("列表最大值为{0}，最小值为{1}".format(max(numList), min(numList)))
    return max(numList), min(numList)


# 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def funTupleAndDict(arg1, arg2=2, *tuple, **dict):
    print(arg1, arg2, *tuple, **dict)


# 定义匿名函数，返回两数乘积
multiply = lambda x, y: x * y

# 写一个函数，返回N的阶乘
def factorial(n):
    for i in range(1, n):
        n *= i
    print(n)
    return n



if __name__ == '__main__':
    functionList([1, 345, 4, 34])
    funTupleAndDict(1, 3, 4, 5, 6, (7, 8), {"姓名": "大饼"})
    print(multiply(2, 4))
    factorial(5)
