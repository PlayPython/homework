
# 创建一个函数，除去字符串前面和后面的空格
def strip():
    s=str(input('请输入一个字符串：'))
    print(s.strip())
strip()

#输入一个字符串，判断是否为回文
def test1():
    s = str(input('请输入一个字符串：'))
    if not s:
        print('请不要输入空字符串！')
        s = input('请重新输入一个字符串：')
    a = reversed(list(s))
    print(list(a))
    if list(a) == list(s):
        print('您所输入的字符串是回文')
    else:
        print('您所输入的字符串不是回文')
test1()
# 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
def number_to_english(num):
    number_0_10 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
    number_11_19 = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    number_20_100 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred']
    if num < 0 or num > 100:
        print('请输入0-100的整数！')
    if num == 0:
        print(number_0_10[0])
    if num == 100:
        print('one-hundred')
    if num >0 and num <= 10:
        print(number_0_10[num])
    if num > 10 and num < 20:
        index = num % 10
        index -= 1
        print(number_11_19[index])
    elif num >= 20 and num < 100:
        a=num//10-2
        b=num%10
        print(number_20_100[a],'-',number_0_10[b])
number_to_english(66)

# 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
# 计算两个日期相差天数，自定义函数名，和两个日期的变量名。
import datetime

def days(str1,str2):
    date1=datetime.datetime.strptime(str1[0:10],"%Y-%m-%d")
    date2=datetime.datetime.strptime(str2[0:10],"%Y-%m-%d")
    num=(date1-date2).days
    print(num)
days('2018-5-2','2017-2-1')
