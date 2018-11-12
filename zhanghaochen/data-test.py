import random
#生成0到20的偶数
print([i for i in range(0,21) if i%2 ==0])
#生成0到20的奇数
print([i for i in range(0,21) if i%2 ])
class Data():
    #判断一个数是否被另外一个函数整除
    def test1(self):
        while True:
            a=input('请输入被除数：')
            b=input('请输入除数：')
            if int(b) == 0:
                print("除数不能为0!")
                continue
            elif int(a) % int(b) == 0:
                print("%s可以被%s整除!" % (a,b))
            else:
                print("%s可以被%s整除" % (a,b))
            break

    #判断一个数字是否为素数
    def test2(self):
        c = int(input('请输入一个整数：'))
        if c < 2:
            print("%s不是素数!" % c)
        else:
            for i in range(2, c):
                if c % i == 0:
                    print("%s不是素数!" % c)
                    break
                else:
                    print("%s是素数!" % c)
                    break
#生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1< N <= 100）和（0<=n<=2**31 -1）。
#然后再随机从这个列表中取N（1<=N<=100）个 随机数出来，对它们排序，然后显示这个子集
    def test3(self):
       l=[]
       y=[]
       while True:
         n=random.randint(0,2**31 -1)
         l.append(n)
         if len(l)<= 100:
            x=sorted(random.sample(l,len(l)))
            y.append(x)
         else:
            break
       print(random.sample(y, 1))

if __name__ == '__main__':
    zhc=Data()
    zhc.test1()
    zhc.test2()
    zhc.test3()