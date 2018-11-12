# 文件过滤，显示一个文件的所有行，忽略以#开始的行
f = open(r"F:\py\1.txt","r")
data= f.readlines()
print(data)
for i in data:
    i.strip(" ")
    if i[0] == "#":
        continue
    else:
        print(i)
f.close()
# 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
f1 = open(r"F:\py\4.txt",'r')
f2 = open(r"F:\py\12.txt",'r')
row = 0
col = 0
for(line1,line2) in zip(f1,f2):
    row+=1
    if line1 != line2:
        col=0
        for(a,b) in zip(line1,line2):
           if a == b:
                col+=1
           else:
                print('第%d行第%d列不一样'%(row,col))
                break
f1.close()
f2.close()

# 统计一个文本中每个单词出现个数
import collections

with open('F:\py\count.txt') as file1:
    word=file1.read().split(' ')

print("\n所有单词组成列表%s"% word)
print("\n各单词出现的次数：%s"%collections.Counter(word))

