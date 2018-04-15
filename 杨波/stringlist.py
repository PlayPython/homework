# 字符串和列表
import random

class Str_and_list():

    def  clear_blank(self):                   # 删除字符串前后空格,lstrip删除前面的空格，rstrip删除后面空格
        str = input("请输入一个字符串：")
        str.strip()
        print(str)

    def judge(self):					      # 判断回文
        while True:
            str = input("请输入一个字符串：\n")
            if len(str) <=2:
                continue
            if str == ''.join(reversed(str)):               # ''.join(reversed(str))
                print("该字符串是回文！")
            else :
                print("该字符串不是回文!")
            break

'''
    def translate(self):                          
        dict=[{'ten':}]
        n=random.randint(0,101)
'''




if  __name__ == "__main__":
    bob = Str_and_list()
    bob.clear_blank()
    bob.judge()