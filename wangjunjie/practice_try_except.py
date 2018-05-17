'''
@author: wangjunjie
@contact: wangjunjie_93@163.com
@file: practice_try_except.py
@time: 2018\5\6 17:06
@desc:使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
'''



def openFile():
    try:
        with open(r"D:\A1\20180506python基础\practice\abc.txt", 'r') as f:
            print(f)
    except Exception as e:
        print(e)
        print("abc.txt文件不存在")


'''
@author: wangjunjie
@contact: wangjunjie_93@163.com
@file: practice_try_except.py
@time: 2018\5\6 17:16
@desc:使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常
'''


def inputOnlyInteger(inputData):
    if type(inputData) != type(1):
        raise ValueError
    else:
        print(inputData)


if __name__ == '__main__':
    openFile()
    inputOnlyInteger(1)
