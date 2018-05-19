# - 创建一个字典，把字典中的键按照字母顺序显示出来
# - 根据已经排序好的字母的键，显示这个字典中的键和值
# - 使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
import random

a={'x':1,'z':234,'y':2,'Z':5}
a_key=sorted(a.keys())
print(a_key)

for b in a_key:
    print(a[b])

random_listA=set([random.randrange(10) for i in range(0,10)])
random_listB=set([random.randrange(10) for i in range(0,10)])

print(random_listA,random_listB)
print(random_listA | random_listB)
print(random_listA & random_listB)