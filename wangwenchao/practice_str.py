# 创建一个函数，除去字符串前面和后面的空格
# - 输入一个字符串，判断是否为回文
# - 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
# - 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数

def str_strip(str1):
    str1=str(str1)
    str2=str1.strip()
    return str2

def judge_palindrome(str1):
    str1=str(str1)
    if list(str1)==list(reversed(str1)):
        print("yes")
    else:
        print('no')


if __name__=='__main__':
    print(str_strip('   d s 4444           '))
    print(judge_palindrome("12321"))
    print(judge_palindrome("123321"))
