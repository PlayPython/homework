import cmath
import random


###-使用循环和算数运算，生成0到20的偶数
for i in range(20):
    if (i%2==0):
        print(i)
###-使用循环和算数运算，生成0到20的奇数
a_list=[i for i in range(20) if i%2!=0]
print(a_list)
