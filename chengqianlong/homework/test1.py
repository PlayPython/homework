#创建一个函数，除去字符串前面和后面的空格
def test():
    a="   dkdjfk  "
    print(a.strip())
test()
#输入一个字符串，判断是否为回文
def test1():
    i = str(input("请输入:"))
    j = reversed(i)
    if len(i)==0:
        print("输入字符串不合法")
    elif list(i) == list(j):
        print("%s是回文"%i)
    else:
        print("%s不是回文" % i)
test1()

#给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
#给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
