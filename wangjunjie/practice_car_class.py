'''
@author: wangjunjie
@contact: wangjunjie_93@163.com
@file: practice_car_class.py
@time: 2018\5\13 0013 16:52
@desc: 写一个关于车的类
'''

class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make ,model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return  long_name.title()

my_new_car = Car('audi', 'a8', 2018)
print(my_new_car.get_descriptive_name())
