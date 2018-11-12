# -*- coding: UTF-8 -*-
#定义一个函数，传入一个由数字组成列表，返回最大最小值
def num_list(num):
    return max(num),min(num)
#定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def fun(*paras,**kw):
    for i in paras:
        print (i)
    for j in kw:
        print(kw[j])
#定义匿名函数，返回两数乘积
multiplication = lambda x,y:x*y
#写一个函数，返回N的阶乘
def factorial(N):
    m=1
    for i in range(1,N+1):
        m = m*i
    return m

#把前面的一些练习题封装成一个个函数实现

if __name__ == '__main__':
    #print(num_list([1,2,3,4]))
    #print(multiplication(2,3))
    #print(factorial(5))
    fun([1,2,3],a=1)

