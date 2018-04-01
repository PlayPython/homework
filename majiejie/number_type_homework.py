###数值类型练习

class Data():
    def even_num(self):#使用循环和算数运算，生成0到20的偶数
        even_num=[]
        for i in range(0,21,2):
            even_num.append(i)
        print(even_num)
    def odd_num(self):#使用循环和算数运算，生成0到20的奇数
        odd_num=[]
        for i in range(1,20,2):
            odd_num.append(i)
        print(i)

    if __name__ == '__main__':

        even_num()
        odd_num()