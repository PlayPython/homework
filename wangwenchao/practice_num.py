# 使用循环和算数运算，生成0到20的偶数
# - 使用循环和算数运算，生成0到20的奇数
# - 写一个函数，判断一个数是否被另外一个数整除
# - 判断一个数字是否为素数
# - 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N
# <= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N对它们排序，然后显示这个子集。
import math
import random

def even_num(num):
    print([i for i in range(0,int(num),2)])

def uneven_num(num):
    print([i for i in range(0,int(num)) if i % 2])

def exact_division(num1,num2):
    if int(num2) % int(num1)== 0:
        return True
    else:
        return False

def judge_prime_num(num):
    num=int(num)
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i ==0:
            return False
    return True

def sort_list():
    a_list=[random.randrange(0,2**31) for i in range(0,random.randint(1,100))]
    return sorted(a_list)
if __name__=='__main__':
    print(even_num(21))
    print(uneven_num(21))
    print(exact_division(2,21))
    print(exact_division(2,20))
    print(judge_prime_num(19))
    print(judge_prime_num(9))
    print(judge_prime_num(4))
    print(sort_list())