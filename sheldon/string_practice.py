# 创建一个函数，除去字符串前面和后面的空格
# - 输入一个字符串，判断是否为回文
# - 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
# - 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数

def judge_plalindrome(string_para):
    a_string = str(string_para)
    if list(a_string) == list(reversed(a_string)):
        return True
    else:
        return False


def convert_numbers_to_letter(number_para):
    number = int(number_para)
    number_list_small = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                         'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    number_list_big = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty', ]
    if number == 0:
        return 'zero'
    elif 0 < number < 20:
        return number_list_small[number - 1]
    elif 20 <= number < 100:
        if str(number)[1] == '0':
            return number_list_big[int(number / 10 - 2)]
        else:
            index_one, index_two = list(str(number))
            index_one, index_two = int(index_one), int(index_two)
            return "{0}-{1}".format(number_list_big[int(index_two - 2)], number_list_small[int(index_one - 1)])
    elif number == 100:
        return 'one hundred'
    else:
        print("please enter the right number, 0 <= number <= 1000")


def test_convert_numbers_to_letter():
    assert convert_numbers_to_letter(100) == "one hundred"


if __name__ == '__main__':
    print(judge_plalindrome("12321"))
    print(judge_plalindrome(12321))
    print(judge_plalindrome("12fsdf321"))
    print(judge_plalindrome("DADA"))
    print(convert_numbers_to_letter(100))
    print(convert_numbers_to_letter(33))
    print(convert_numbers_to_letter(40))
    print(convert_numbers_to_letter(6))
    print(convert_numbers_to_letter(99))
    print(convert_numbers_to_letter(11))
