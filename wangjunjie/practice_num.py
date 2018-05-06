'''
@author: wangjunjie
@contact: wang.junjie@trs.com.cn
@file: practice_num.py
@time: 2018-04-01 20:35
@desc: 数值类型练习

'''
import random

# - 使用循环和算数运算，生成0到20的偶数（方法一）
for x in range(21):
    if x % 2 == 0:
        print(x)

# - 使用循环和算数运算，生成0到20的偶数（方法二）
print([i for i in range(0, 21) if i % 2 == 0])

# - 使用循环和算数运算，生成0到20的奇数
print([i for i in range(0, 21) if i % 2])


# - 写一个函数，判断一个数是否被另外一个函数整除
def isDivided(y, x):
    if x % y == 0:
        print("{0}能被{1}整除".format(y, x))
    else:
        print("{0}不能被{1}整除".format(y, x))


'''- 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N
<= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N（1<=N<=100）个
随机数出来，对它们排序，然后显示这个子集。'''
N = random.randint(2, 100)
# 随机获取一个指定范围内的整数
randlist = random.sample(range(0, 2 ** 31 - 1), N)
# 从一个序列中随机序列(这里string，tuple，列表都可以看做是序列)获取含有N个元素，以列表形式返回
randlist.sort()
print(randlist)

if __name__ == '__main__':
    isDivided(2, 9)
