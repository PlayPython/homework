'''
@author: wangjunjie
@contact: wang.junjie@trs.com.cn
@file: practice_str_and_list.py
@time: 2018-04-01 21:07
@desc: 字符串和列表

'''


# - 创建一个函数，除去字符串前面和后面的空格
def removeSpace(str):
    print(str.strip())


# - 输入一个字符串，判断是否为回文
def plalindrome():
    a = input("请输入字符串：")
    b = str(a)

    for i in range(int(len(b) / 2)):
        if b[i] == b[len(b) - i - 1]:
            print("'{0}'是回文".format(a))
        else:
            print("'{0}'不是回文".format(a))


# - 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
def number_to_english(num):
    number_0_10 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    number_11_19 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                    'nineteen']
    number_20_100 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']
    number = int(num)
    transfer = ""
    if number < 0 or number > 100:
        print(transfer)
    if number == 0:
        transfer = number_0_10[0]
        print(transfer)
    if number == 100:
        transfer = number_20_100[-1]
        print(transfer)
    if number <= 10:
        transfer = number_0_10[number]
        print(transfer)
    elif number > 10 and number <= 20:
        index = number % 10
        index -= 1
        transfer = number_11_19[index]
        print(transfer)
    elif number > 20 and number < 100:
        index = int(number / 10)
        index -= 2
        index2 = number % 10
        transfer = number_20_100[index]
        transfer1 = number_0_10[index2]
        print(transfer,'-',transfer1)



if __name__ == '__main__':
    removeSpace('          2018年4月1日21:10:42    ')
    # plalindrome()
    number_to_english(79)
