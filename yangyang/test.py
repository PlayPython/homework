# def square(x):  # 计算平方数
# 	return x ** 2
#
#
# result = map(square, [1, 2, 3, 4, 5])  # 计算列表各个元素的平方
# result1 = (map(lambda x: x ** 2, [1, 2, 3, 4, 5]))  # 使用 lambda 匿名函数
# result2 = (map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))  # 提供了两个列表，对相同位置的列表数据进行相加
# print(list(result))
# print(list(result1))
# print(list(result2))
#
#
# def is_odd(n):
# 	return n % 2 == 1
#
#
# newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 过滤奇数
# print(list(newlist))

# import os, datetime
#
# base_dir = 'c:/'
# list = os.listdir(base_dir)  # 列出base_dir下的目录和文件
# filelist = []
# for i in range(0, len(list)):
# 	path = os.path.join(base_dir, list[i])  # 连接目录与文件名或目录
# 	if os.path.isfile(path):
# 		filelist.append(list[i])
#
# for i in range(0, len(filelist)):
# 	path = os.path.join(base_dir, filelist[i])
# 	if os.path.isdir(path):
# 		continue
# 	timestamp = os.path.getmtime(path)
# 	print(timestamp)
# 	ts1 = os.stat(path).st_mtime
# 	print(ts1)
#
# 	date = datetime.datetime.fromtimestamp(timestamp)
# 	print(list[i], ' 最近修改时间是: ', date.strftime('%Y-%m-%d %H:%M:%S'))

import math


def is_prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


primes = filter(is_prime, range(2, 100))


print(list(primes))


# def count(n):
# 	while n > 0:
# 		yield n  # 生成值：n
# 		n -= 1
#
#
# print(list(count(5)))