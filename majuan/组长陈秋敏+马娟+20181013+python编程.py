#使用循环和算数运算，生成0到20的偶数
l1=[]
for i in range(0,21):
    if i % 2 == 0:
        l1.append(i)
print(l1)

#使用循环和算数运算，生成0到20的奇数
l2=[]
for i in range(0,21):
    if i % 2 != 0:
        l2.append(i)
print(l2)

#写一个函数，判断一个数是否被另外一个数整除
def chu(a,b):
    if a % b == 0:
        print('%d能被%d整除'%(a,b))
    else:
        print('%d不能被%d整除'%(a,b))

#判断一个数字是否为素数
num = int(input('请输入一个数：'))
for i in range(2,num):
    if num % i == 0:
        print('%d不为素数'%num)
        break
    else:
        print('%d为素数'%num)
        break

#创建一个函数，除去字符串前面和后面的空格
def qkg(a):
    print(a.strip())

#输入一个字符串，判断是否为回文
def hw(x):
    a=len(x)
    if x[:1]==x[-a:]:
        print("是回文")
    else:
        print("不是回文")

#创建一个字典，把字典中的键按照字母顺序显示出来
zd= {"a": "b", "c": "d", "e": "f", "x": "y"}
def zidian():
    l = list(zd.keys())
    l.sort()
    print(l)







