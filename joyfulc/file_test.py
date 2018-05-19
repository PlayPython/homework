
#文件过滤，显示一个文件的所有行，忽略以#开始的行
f = open("test.txt","r")
flist = f.readlines()
for x in range(0,len(flist)):
    if flist[x][0]=="#":
        continue
    else:
        print(flist[x],end="")

#比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
f1 = open("test.txt","r")
f2 = open("test2.txt","r")
flist1=f1.readlines()
flist2=f2.readlines()
for x in range(0,len(flist1)):
    #取出每一行
    flist3=flist1[x]
    flist4=flist2[x]
    if x<len(flist2)-1:
        for y in range(0,len(flist3)):
            #针对一行每个字进行对比
            if flist3[y]!=flist4[y]:
                print("第{0}行，第{1}列，出现了不一样的内容".format(x,y))
                break
            else:
                continue
    else:
        break

#统计一个文本中每个单词出现个数


if __name__=="__main__":
    pass