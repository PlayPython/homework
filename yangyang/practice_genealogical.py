'''
@author: yangyang
@contact: doubley9207@163.com
@file: practice_genealogical.py
@time: 2018\5\22 17:50
@desc:正则表达式,迭代器练习
'''
#  正则表达式
# - 匹配用空格分隔的任意一对单词，比如名和姓
# - 匹配以www.和.com结束的域名
# - 列出一个文件夹下所有文件的修改时间，获取文件的修改时间戳，比如HH:MM
import re, os, time


class RegExp:
	def __init__(self, text):
		self.text = text
	
	def space(self):
		matchspace = re.search(r'(\w+)\s(\w+)', self.text)
		print(matchspace)
	
	def network(self):
		matchnet = re.search('^www.(\S+).com$', self.text)
		print(matchnet)
	
	def filename_time(self, path):
		self.path = path
		base_dir = self.path
		list = os.listdir(base_dir)
		for i in range(len(list)):
			path = os.path.join(base_dir, list[i])
			# makefiletime = os.path.getmtime(path)
			makefiletime = time.localtime(os.stat(path).st_mtime)
			print(path)
			# print(time.strftime("%Y-%m-%d %H:%M:%S", makefiletime))
			print(time.strftime("%H:%M", makefiletime))


# 迭代器
# - 构造一个能够输出100以内的所有奇数的迭代器，打印里面的值
# - 用yield构造一个返回质数函数，从2开始，每次调用返回下一个更大的质数
def odd_number():
	newlist = filter(lambda x: x % 2 == 1, range(1, 101))
	print(list(newlist))


def prime_number(num):
	for i in range(2,num):
		if


if __name__ == '__main__':
	# regexp = RegExp('hello yangyang')
	# regexp.filename_time('c:/')
	# odd_number()
	f = prime_number(4)
	print(next(f))