# 模块和类
# 导入自定义模块里面的函数，并使用
from test20180506 import factorial
factorial(4)
# 安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
# github API https://developer.github.com/v3/
'''
import requests as requests_api
#re=requests_api.get("https://github.com/whatever")
re=requests_api.get("https://api.github.com?callback=foo")
print(re.content)
'''
# 定义一个类，同时具有这样数据结构，实现四个方法
# unshift() 添加列表第一个元素
# push() 添加到列表最后一个元素
# pop() 返回并删除列表最后一个元素

import copy
class Data_structure():
    def __init__(self,datas):
        self.datas=datas
    def push(self,a):
        self.a=a
        b=copy.deepcopy(self.datas)
        b.append(self.a)
        return b
    def pop(self):
        b = copy.deepcopy(self.datas)
        b=b[:-1]
        return b



num=Data_structure([1,2,3,4,5])
print(num.push(3))
print(num.pop())

# 定义一个类，实现深度优先搜索和广度优先搜索两个方法

# 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承

class Pet():
    def __init__(self,name):
        self.name=name
    def run(self):
        print("%s can run" % self.name)

class Dog(Pet):
    def bark(self):
        print(self.run())
        print("%s is 汪汪汪" % self.name)

class Cat(Pet):
    def meow(self):
        print(self.run())
        print("%s is 喵喵喵" % self.name)


dog=Dog("狗")
dog.bark()
cat=Cat("猫")
cat.meow()
