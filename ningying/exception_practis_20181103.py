# -*- coding: UTF-8 -*-
#使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
def open_file_error(filen_ame):
    try:
        open(filen_ame,"r")
    except FileNotFoundError as e:
        print(e)
#使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常
def integer(num):
    if isinstance(num,int) and num>0:
        print (num)
    else:
        raise Exception

if __name__ == '__main__':
    #open_file_error("1.txt")
    integer(0)