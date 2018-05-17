# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 21:32
# @Author  : mdl
# @Email   : 1271737949@qq.com
# @File    : string_list_practice.py
# @Software: PyCharm

'''字符串和列表'''

# - 创建一个函数，除去字符串前面和后面的空格
def str_strip():
    r="    rrrsdf fff  "
    print(r.strip())
# str_strip()

# - 输入一个字符串，判断是否为回文
def palindrome():
    s=input("请输入字符串：")
    if isinstance(s,str):
        print()
    else:
        print("请重新输入字符串！")
palindrome()
# - 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100



# - 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数