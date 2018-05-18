# 使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
def file(files):
	try:
		f = open(files, 'r')
	except FileNotFoundError:
		print('The file is not find!')


# 使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常


def rasie_error():
	number = input('请输入一个数:')
	try:
		if isinstance(int(number), int) and int(number) > 0:
			print(number)
		else:
			pass
	except Exception as e:
		raise Exception(e)


# 定义一个函数，传入一个由数字组成列表，返回最大最小值
def function(*args):
	args = list(args)
	print('max:', max(args))
	print('min:', min(args))


# 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def parameter(num, *args, **dircty):
	print(num)
	print(dircty)
	for var in args:
		print(var)


# 定义匿名函数，返回两数乘积
num = lambda x, y: x * y


# 写一个函数，返回N的阶乘
def factorial(num):
	if isinstance(num, int):
		if num == 1 or num == 0:
			print('0! = 1!:', 1)
		elif num < 0:
			print('负数没有阶乘')
		else:
			n = 1
			for i in range(2, num + 1):
				n = n * i
			print('%s 的阶乘是%s' % (num, n))
	else:
		print('请输入一个正整数')


# 把前面的一些练习题封装成一个个函数实现
#
# 模块和类
#
# 导入自定义模块里面的函数，并使用安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
# github API https://developer.github.com/v3/

# 定义一个类，同时具有堆栈的数据结构，实现四个方法
# shift() 返回并删除列表最后一个元素
# unshift() 添加列表第一个元素
# push() 添加到列表最后一个元素
# pop() 返回并删除列表最后一个元素
class Storage():
	def __init__(self, l):
		self.l = l
		self.l = [i for i in range(1, l)]
	
	def shift(self):
		# shift()返回并删除列表最后一个元素
		print (self.l.pop())
		print (self.l)
	
	def unshift(self, num):
		# unshift() 添加列表第一个元素
		self.l.insert(0, num)
		print (self.l)
	
	def push(self, num):
		# push() 添加到列表最后一个元素
		self.l.append(num)
		print (self.l)


# 定义一个类，实现深度优先搜索和广度优先搜索两个方法

# 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
class Pet():
	def __init__(self, colour, size, sex, age):
		self.colour = colour
		self.size = size
		self.sex = sex
		self.age = age
	
	def feed(self):
		print ('吃东西')
	
	def sleep(self):
		print ('睡觉')
	
	def run(self):
		print ('跑步')


class Dog(Pet):
	def mydog(self):
		print ('我的小狗的年龄', self.age)


class Cat(Pet):
	def mycat(self):
		print ('我的小猫的颜色', self.colour)


if __name__ == '__main__':
	# file('test.txt')
	# rasie_error()
	# function(1, 2, 3, 4, 5, 76)
	# parameter(1, 2, 34, 5, 5, 66, m = 25, n = 16)
	# print(num(4, 5))
	# factorial(4)
	# m = Storage(6)
	# m.shift()
	# m.unshift(10)
	# m.push(1)
	mypet = Dog('red', 'small', 'female', 2)
	mypet1 = Cat('black', 'big', 'female', 3)
	mypet.mydog()
	mypet1.mycat()
