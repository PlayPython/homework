# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 16:42
# @Author  : mdl
# @Email   : 1271737949@qq.com
# @File    : exception_practice.py
# @Software: PyCharm


#- 使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
def  open_file():
    try:
        file=open("te3st","r")
    except Exception as e:
        print(e)
        print("找不到文件!")
# open_file()


#使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常

def input_num():
    b=input("请输入正整数：")
    if isinstance(b,int) and b>=0:
        print("ok")
    else:
        raise Exception("请重新输入！")

input_num()






