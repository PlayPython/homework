def functionfile(files):
	try:
		f = open(files, 'rw')
	except BaseException:
		print('The file is not find')
	else:
		print('da kai wen jian chenggong')


def rasie_error():
	num = input('请输入一个数:')
	try:
		if isinstance(int(num), int) and int(num) > 0:
			print(num)
		else:
			pass
	except Exception as e:
		raise Exception(e)


# def rasie_error():
# 	num = input('请输入一个数:')
# 	try:
# 		if type(num) != isinstance(num, int):
# 			raise Exception('error')
# 		elif num < 0:
# 			raise Exception('error1')
# 	except Exception:
# 		raise
# 	else:
# 		print(num)


def fun(*num):
	num = list(num)
	print('max:%s' % max(num))
	print('min:%s' % min(num))


def parameter(num, name = 'yangyang', *args, **dircty):
	print(num)
	print(name)
	print(dircty)
	for var in args:
		print(var)


def factorial(num):
	if isinstance(num, int):
		if num == 1 or num == 0:
			print('0! = 1!:', 1)
		elif num < 0:
			print ('负数没有阶乘')
		else:
			n = 1
			for i in range(2, num + 1):
				n = n * i
			print('%s 的阶乘是%s' % (num, n))
	else:
		print ('请输入一个正整数')


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
	# fun(1, 2, 3, 4, 5, 76)
	# parameter(1, 2, 3, 4, 5, 6, 7, m = 2)
	# factorial(-1)
	# m = Storage(6)
	# m.shift()
	# m.unshift(10)
	# m.push(1)
	# mypet = Dog('red', 'small', 'female', 2)
	# mypet1 = Cat('black', 'big', 'female', 3)
	# mypet.mydog()
	# mypet1.mycat()
