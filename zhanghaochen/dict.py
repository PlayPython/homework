import random
# 创建一个字典，把字典中的键按照字母顺序显示出来
dict={'a':1,'c':2,'b':3,'d':4}
s=dict.keys()
print(sorted(s))
m=sorted(s)
# 根据已经排序好的字母的键，显示这个字典中的键和值
for i in m:
    v=dict.get(i)
    print(v)
# 使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
l1=[0,1,2,3,4,5,6,7,8,9]
l2=[0,1,2,3,4,5,6,7,8,9]
A=random.sample(l1,10)
B=random.sample(l1,10)
