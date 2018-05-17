# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 20:58
# @Author  : mdl
# @Email   : 1271737949@qq.com
# @File    : numerical_practice.py
# @Software: PyCharm
import random

'''数值类型练习'''

#使用循环和算数运算，生成0到20的偶数
def  even_num():
    for i in range(0,21):
        if i%2==0:
            print(i,"是偶数")
            continue

#使用循环和算数运算，生成0到20的奇数
def odd_num():
    for i in range(0,21):
        if i%2!=0:
            print(i,"是奇数")
            continue

#写一个函数，判断一个数是否被另外一个数整除
def aliquot(one,two):
    if isinstance(one,int) & isinstance(two,int):
        if one%two==0:
            print("{0}能被{1}整除".format(one,two))
        elif two%one==0:
            print("{0}能被{1}整除".format(two,one))
        else:
            print("都不能被整除")
    else:
        print("请重新输入！")
#aliquot(3,6)

#生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N<= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N（1<=N<=100）个随机数出来，对它们排序，然后显示这个子集。

def random_num():
    N=random.randint(1,100)   #列表长度
    NN=[]
    print(N)
    for r in range(N):
        NN.append(random.randint(0,2**31-1))
    NN.sort()
    print(NN)
# random_num()