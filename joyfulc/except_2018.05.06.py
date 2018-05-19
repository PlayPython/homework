
#- 使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
def except_test():
    try:
        f = open("haha.txt",'r')
    except FileNotFoundError as e:
        print(e)
        print("文件可能不存在")

#- 使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常
def raise_except_test(s1):
    try:
         if isinstance(int(s1), int) and int(s1) > 0:
             print("你输入的确是是个数字！")
    except:
        print("老实交代，你是不是输入了字母？")
        raise

if __name__ == '__main__':
    print("\n①、捕获指定异常练习")
    except_test()
    print("\n②、强制抛出异常练习")
    s1 = input("请随意输入一个数字:")
    raise_except_test(s1)
