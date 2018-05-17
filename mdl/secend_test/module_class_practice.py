# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 15:15
# @Author  : mdl
# @Email   : 1271737949@qq.com
# @File    : module_class_practice.py
# @Software: PyCharm

# - 导入自定义模块里面的函数，并使用
import random
def import_module(min,max):
    num=random.random()
    print("第一个随机数为：",num)
    twonum=random.randint(min,max)
    print("第二个随机数为：",twonum)
# import_module(1,90)

# - 安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
#   + github API https://developer.github.com/v3/
import requests as ree
def requests_test():
    r=ree.get('https://developer.github.com/v3/')
    print (r.text)
# requests_test()

# - 定义一个类，同时具有堆栈的数据结构，实现四个方法
#   + shift() 返回并删除列表最后一个元素
#   + unshift() 添加列表第一个元素
#   + push() 添加到列表最后一个元素
#   + pop()  返回并删除列表最后一个元素
class stack:
    def shift_test(self):
        print("删除列表最后一个元素之前为：",list)
        del list[len(list)-1]
        print("删除列表最后一个元素后为：",list)

    def unshift_test(self):
        print("添加列表第一个元素之前为：", list)
        list.append(list[0])
        print("添加列表第一个元素后为：", list)

    def push_test(self):
        print("添加到列表最后一个元素之前为：", list)
        list.append(list[len(list)-1])
        print("添加到列表最后一个元素后为：", list)

    def pop_test(self):
        print("删除列表最后一个元素之前为：", list)
        list.pop()
        print("删除列表最后一个元素后为：", list)




# - 定义一个类，实现深度优先搜索和广度优先搜索两个方法


# - 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
class pet():
    def __init__(self,food_name,time):
        self.food_name=food_name
        self.time=time
    def eat(self):
        print("pet使用的食物是：",self.food_name)

    def sleep(self):
        print("pet睡觉时间时长为：",self.time)

class dog(pet):
    def eat(self):
        print("dog使用的食物是：",self.food_name)
class cat(pet):
    def eat(self):
        print("cat使用的食物是：", self.food_name)
if __name__=='__main__':
    list=[2,90,39,44]
    # stack().shift_test()
    # stack().unshift_test()
    # stack().push_test()
    # stack().pop_test()
    p=pet("bannaner","8")
    p.eat()
    p.sleep()
    d=dog("骨头","5")
    d.eat()
    d.sleep()
    c=cat("小鱼",7)
    c.eat()