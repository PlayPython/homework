
#- 定义一个函数，传入一个由数字组成列表，返回最大最小值
def list_text():
    list1 = [13,-77,2,39,83,6,55,-3]
    s1=max(list1)
    s2=min(list1)
    print("{0}中最大的：{1},最小的：{2}".format(list1,s1,s2))

#- 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def VarArgs(arg1,*tunple,**theRest):
    print("第一个普通参数是{0}".format(arg1))
    print("第二个不定参数是{0}".format(tunple))
    print("第三个字典参数是{0}".format(theRest))
    for key in theRest:
        print("字典参数是{0}".format(theRest[key]))

#- 定义匿名函数，返回两数乘积
def niming():
    s3=input("请随意输入一个数字s3:")
    s4=input("请再输入一个数字s4:")
    multiply = lambda x,y:x*y
    print("{0}*{1}={2}".format(s3,s4,multiply(int(s3),int(s4))))

#- 写一个函数，返回N的阶乘
def jiecheng(m):
    j=m
    for n in range(1,m):
        if n<m:
            j=j*n
    print("{0}的阶乘是{1}".format(m,j))

#- 把前面的一些练习题封装成一个个函数实现
if __name__ == '__main__':
    print("\n①、返回列表中的最大/最小值")
    list_text()
    print("\n②、匿名函数练习")
    niming()
    print("\n③、参数练习")
    VarArgs(1,2,3,4,key5=5,key6=6)
    print("\n④、阶乘练习")
    N = input("请随意输入一个数字N:")
    jiecheng(int(N))
