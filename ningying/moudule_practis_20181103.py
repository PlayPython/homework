# -*- coding: UTF-8 -*-
import requests as requ
#导入自定义模块里面的函数，并使用
from function_practis import num_list
a = num_list([1,2,3])
#print(a)
#安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
#github API https://developer.github.com/v3/
a = requ.get("https://api.github.com/users/octocat/orgs")
#print(a.text)
#定义一个类，同时具有这样数据结构，实现三个方法
#unshift() 添加列表第一个元素
#push() 添加到列表最后一个元素
#pop() 返回并删除列表最后一个元素
class MunCase:
    def __init__(self,muncase):
        self.muncase = muncase
    def unshift(self,i):
        muncase = self.muncase.copy()
        muncase.insert(0,i)
        return muncase
    def push(self,i):
        muncase = self.muncase.copy()
        muncase.append(i)
        return muncase
    def pop_p(self):
        muncase = self.muncase.copy()
        muncase.pop()
        return muncase
#定义一个类，实现深度优先搜索和广度优先搜索两个方法
#class Search:

#定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
class Pet:
    def __init__(self,eye,mouth,nose):
        self.eye = eye
        self.mouth = mouth
        self.nose = nose
    def running(self):
        print("%d眼，%d口，%d鼻，会跑" % (self.eye,self.mouth,self.nose))
    def eatting(self):
        print("会吃")
class Cat(Pet):
    def __init__(self,eye,mouth,nose,type,character):
        super(Cat, self).__init__(eye,mouth,nose)
        self.type = type
        self.character = character
    def running(self):
        super(Cat, self).running()
        print("我是%s,性格%s" % (self.type,self.character))
    def eatting(self):
        super().eatting()
        print("爱吃鱼")
class Dog(Pet):
    def __init__(self,eye,mouth,nose):
        super(Cat, self).__init__(eye,mouth,nose)

#更新示例中car的display_car方法，使其通用性更强，比如打印每个参数，而不只是父类的几个参数
if __name__ == '__main__':
    #mun = MunCase([1,2,3])
    #print(mun.unshift(0))
    #print(mun.push(4))
    #print(mun.pop_p())
    m = Cat(2,1,1,"猫猫","高冷")
    m.eatting()
    m.running()

