# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 21:56
# @Author  : mdl
# @Email   : 1271737949@qq.com
# @File    : file_conditionalstatements_practice.py
# @Software: PyCharm

from math import sqrt

'''文件和条件语句练习'''

#文件过滤，显示一个文件的所有行，忽略以#开始的行
def print_row():
    f = open('E:\homework\mdl\print_row.txt', 'r')
    # print f.readline
    countNum = 0
    num = 0
    # 利用一次循环算出有几行数据
    for eachLine in f.readlines():
        # 判断一行的开头字符是不是 #开始
        if str(eachLine)[0] == '#':
            continue
        else:
            print ("'the line without '#': ", eachLine)
        countNum += 1
    print ( 'the numbers of line is ', countNum)
    # 关闭文件
    f.close()
# print_row()
#比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
def compare_file():
    f1 = open("E:\homework\mdl\print_row.txt", 'r')
    f2 = open("E:\homework\mdl\print_row2.txt", 'r')
    row = 0  # 记录出现不同字符的行
    for (line1, line2) in zip(f1, f2):
        row += 1
        if line1 == line2:
            pass
        else:
            col = 0;
            print(row)
             # 记录不同字符出现的列号
            for (a, b) in zip(line1, line2):
                if a == b:
                    col += 1
                else:
                    print(col)

    f1.close()
    f2.close()
# compare_file()
#写一个函数，返回N的阶乘
def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    print(result)
factorial(4)
#判断一个数字是否为素数
def prime_num(num):
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "不是质数")
                break
        else:
            print(num, "是质数")
    else:
        print(num, "不是质数")
# prime_num(34)

#统计一个文本中每个单词出现个数
def count_text(s):
    # 先把字符串分割成单个单词列表
    list1 = s.split()
    # 把列表转为结合，为了去除重复的项
    set1 = set(list1)
    # 把集合转为列表，集合元素没有顺序，没有索引属性，而列表有
    list2 = list(set1)
    # 新建一个空的字典
    dir1 = {}
    for x in range(len(list2)):
        dir1[list2[x]] = 0  # 字典值初始为0
        for y in range(len(list1)):
            if list2[x] == list1[y]:
                dir1[list2[x]] += 1
    print( dir1)

# count_text('hello you welcom to hello you to')