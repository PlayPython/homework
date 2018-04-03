# - 文件过滤，显示一个文件的所有行，忽略以#开始的行
# - 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
# - 写一个函数，返回N的阶乘
# - 判断一个数字是否为素数
# - 统计一个文本中每个单词出现个数

import codecs

with codecs.open('file.py', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if not line.strip().startswith("#"):
            print(line)
