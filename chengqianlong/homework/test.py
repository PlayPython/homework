import random
#使用循环和算数运算，生成0到20的偶数
print([i for i in range(0,21) if i % 2])
#使用循环和算数运算，生成0到20的奇数
print([i for i in range(0,21) if i % 2 ==0])
#写一个函数，判断一个数是否被另外一个函数整除
def work(i,j):
    if i % j == 0:
        print("%d能被%d整除"%(i,j))
    else:
        print("%d不能被%d整除"%(i,j))
#work(6,3)
#work(6,4)
#判断一个数字是否为素数
def test():
    i = int(input("请输入正整数："))
    for j in range(2,i+1):
        if i % j != 0 and i % i == 0:
            print("%d是素数"%i)
            break
        else:
            print("%d不是素数" % i)
            break
#test()
#生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N <= 100）和
#0<=n<=2**31 -1）。然后再随机从这个列表中取N（1<=N<=100）个 随机数出来，对它们排序，然后显示这个子集。
def test1():
    list=[]
    N=int(random.uniform(2,101))
    for N in range(N+1):
        n=int(random.uniform(0,2**31 -1))
        list.append(n)
    sorted(list)
    print(list)
test1()


