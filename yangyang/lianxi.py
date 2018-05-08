def file(files):
	try:
		f = open(files, 'rw')
	except BaseException, error:
		print('The file is not find')
	else:
		print('da kai wen jian chenggong')


def rasie_input():
	try:
		num = int(input('请输入一个数:'))
		if num > 0:
			return num
	except Exception:
		raise Exception('请输入一个正整数')


if __name__ == '__main__':
	file('test.txt')
