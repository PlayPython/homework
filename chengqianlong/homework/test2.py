#创建一个字典，把字典中的键按照字母顺序显示出来
dict={'d':1,'b':2,'h':3,'z':4}
a=dict.keys()
print(sorted(a))
#根据已经排序好的字母的键，显示这个字典中的键和值
d=sorted(a)
for i in d:
    s=dict.get(i)
    print(s)
#使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
