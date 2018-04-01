import random
import math

# 打印π
print(math.pi)
##数值类型练习
# - 使用循环和算数运算，生成0到20的偶数
for i in range(0, 21, 2):
    print(i)

# - 使用循环和算数运算，生成0到20的奇数
for i in range(1, 21, 2):
    print(i)
#- 写一个函数，判断一个数是否被另外一个数整除
def divide_exactly(x,y):
    if x%y==0:
        print("yes")
    else:
        print("no")
divide_exactly(8,2)
'''
- 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N
<= 100）和（0<=n<=2**31 -1）。然后再随机从这个列表中取N（1<=N<=100）个
随机数出来，对它们排序，然后显示这个子集。
备注：就是在将这个列表排个序；
'''
def random_list():
    N = random.randrange(1, 101, 1)
    list = []
    for i in range(N):
        n = random.randrange(0, 2 ** 31, 1)
        list.append(n)
    print(sorted(list))
    print(N)
random_list()

