# 创建一个函数，除去字符串前面和后面的空格
# - 输入一个字符串，判断是否为回文
# - 给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100
# - 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
import datetime


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
    number_list_big = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', ]
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


# 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
# 计算从0年开始到对应日期的天数，然后相减
def count_days(start_date="11/9/19", end_date="11/9/19"):
    return _convert_date_to_days(end_date) - _convert_date_to_days(start_date)


def _convert_date_to_days(date=None):
    every_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isinstance(date, str):
        numbers = date.split("/")
        month, day, year = int(numbers[0]), int(numbers[1]), int(numbers[2])
        days_year, days_month = 0, 0
        for num in range(0, year):  # 假设从0年开始计数，公元0年是闰年
            if _judge_leap_year(num):
                days_year = days_year + 366
            else:
                days_year = days_year + 365
        if _judge_leap_year(year):  # 月份从1开始，没有0月，所以1月时候不计算月
            if month > 2:
                days_month = sum(every_month_days[:month - 1]) + 1
            else:
                days_month = sum(every_month_days[:month - 1])
        else:
            days_month = sum(every_month_days[:month - 1])
        return days_year + days_month + day
    else:
        raise AssertionError("input parameter type is wrong")


def _judge_leap_year(year_num):
    if (year_num % 4 == 0 and year_num % 100 != 0) or (year_num % 400 == 0):
        return True
    else:
        return False


def test_judge_leap_year():
    assert _judge_leap_year(0) is True
    assert _judge_leap_year(4) is True
    assert _judge_leap_year(3) is False
    assert _judge_leap_year(100) is False
    assert _judge_leap_year(400) is True
    assert _judge_leap_year(401) is False


def test_convert_date_to_days():
    assert _convert_date_to_days("1/9/1") == 375
    assert _convert_date_to_days("1/1/1") == 367
    assert _convert_date_to_days("2/1/1") == 398
    assert _convert_date_to_days("3/1/1") == 426
    assert _convert_date_to_days("2/29/4") == 1521


def test_count_days():
    assert count_days("1/9/1", "1/16/1") == 7
    d1 = datetime.datetime(2005, 2, 16)
    d2 = datetime.datetime(2004, 12, 31)
    assert (d1 - d2).days == count_days("12/31/2004", "2/16/2005")
    d1 = datetime.datetime(2012, 4, 22)
    d2 = datetime.datetime(1986, 1, 31)
    assert (d1 - d2).days == count_days("1/31/1986", "4/22/2012")


def test_convert_numbers_to_letter():
    assert convert_numbers_to_letter(100) == "one hundred"
    assert convert_numbers_to_letter(33) == "thirty-three"
    assert convert_numbers_to_letter(40) == "forty"
    assert convert_numbers_to_letter(6) == "six"
    assert convert_numbers_to_letter(99) == "ninety-nine"
    assert convert_numbers_to_letter(11) == "eleven"


if __name__ == '__main__':
    print(judge_plalindrome("12321"))
    print(judge_plalindrome(12321))
    print(judge_plalindrome("12fsdf321"))
    print(judge_plalindrome("DADA"))
    res = _convert_date_to_days("1/9/1")
    print(res)
