# -*- coding: utf-8 -*-
import re
import os,datetime
import threading
import requests
from time import ctime,sleep
class multithread():
    """
 正则表达式
    """
##- 匹配用空格分隔的任意一对单词，比如名和姓
    def regular_blank(slef,name):

        print(re.sub(' ','\n',name))##出现空格就换行


##- 匹配以www.和.com借宿的域名
    def regular_dns(slef,dns):
        pattern = re.compile(r'www.(.+?).com')##匹配www.与.com之间的字符串
        print((re.match(pattern,dns)).group())

##- 列出一个文件夹下所有文件的修改时间，获取文件的修改时间戳，比如HH:MM
    def regular_filetime(slef,path):
        filelist=[]
        list=os.listdir(path)##列出目录下的文件及文件夹放入list
        #print(list)
        for i in range(len(list)):
            filepath=os.path.join(path,list[i])#将目录与文件名拼接起来
            if os.path.isfile(filepath):###判断拼接的目录是否是文件
                filelist.append(filepath)
                #print(filepath)
        if len(filelist)==0:
            print("该目录下没有文件")
        else:
            #print(filelist)
            for j in range(len(filelist)):
                #print(os.path.getmtime(filelist[j]))
                date = datetime.datetime.fromtimestamp(os.path.getmtime(filelist[j]))
                print(filelist[j]+'最近修改时间为：'+date.strftime("%Y-%m-%d %H:%M:%S"))

    """
迭代器
    """
###用yield构造一个返回质数函数，从2开始，每次调用返回下一个更大的质数
    def prime_number(slef,n):  ###生成2到n的迭代器
        a = 2
        for i in range(1,n):
            yield a
            a=a+1
    def filter_nu(slef,a):
        return lambda x:x%a>0
    """
filter: 过滤符合条件的可迭代序列
        1.参数1: 函数 或 lambda表达式
        2.参数2: 可迭代序列
    """
    def produce_prime_number(slef,n):
        b=slef.prime_number(n)
        while True:
            c=next(b)
            yield c
            b=filter(slef.filter_nu(c),b)  ###过滤取余大于0的数字

    """
 多线程
    """
###- 尝试使用多线程方法访问github API并拿取数据，比如同时哪取20个用户的id信息

def funx_thread():
    lock=threading.Lock()##创建锁
    lock.acquire()##取锁
    obj=requests.get('https://github.com/PlayPython/homework/tree-commit/5ad3bb99f7cef48fb6121cb131b6fe9025ae44cd')
    print(obj.cookies)##打印cookies
    sleep(5)
    lock.release()  ###取消锁


def threadfunc(n):
    threads=[]   ###线程池
    print("starrt %s" % ctime())
    for i in range(n):
        threads.append(threading.Thread(target=funx_thread))
    #print(threads)
    for j in  threads:
        j.start()   ###开始进程
    for t in threads:
        t.join()       ####阻塞
    print ("over %s" % ctime())

if __name__ == "__main__":
    mod=multithread()   ###创建对象
    mod.regular_blank("Mr hde")
    mod.regular_dns("www.baidu.com")
    mod.regular_filetime("c:")
    threadfunc(100)
    #g=mod.produce_prime_number(10)
    #g.__next__()
    for j in mod.produce_prime_number(50):#n以内的质数
        print(j)