# - 创建一个字典，把字典中的键按照字母顺序显示出来
# - 根据已经排序好的字母的键，显示这个字典中的键和值
# - 使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
import random

a = {'a': 1, 'A': 10, 'b': 2, 'c': 3, 'C': 30}

a_key = a.keys()
print(sorted(a_key))

print("=" * 20)
for key in a_key:
    print(a[key])

print("=" * 20)
# create random numbers
A_random_list = set([random.randrange(10) for i in range(10)])
B_random_list = set([random.randrange(10) for i in range(10)])
C_random_list=set([random.randrange(20) for i in range(9)])
print((C_random_list))
print(A_random_list, B_random_list)
print(A_random_list & B_random_list)
print(A_random_list | B_random_list)
# print(b_random_list)
