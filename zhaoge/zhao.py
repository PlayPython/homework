#偶数
for i in range(0,21,2):
	print(i)

#奇数
for i in range(1,20,2):
	print(i)

#整除
import random
def zhengchu(a,b):
    '''a=input('输入A')
    b=input('输入b')'''
    if a%b==0:
        print('整除')
    else:
        print('不能整除')

def random_list():
    random.randrange(0,2**31)

if __name__ == '__main__':
    zhengchu(1,2)

--------我是4.10分割线---------------
