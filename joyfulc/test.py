
def jiecheng(m):
    j=m
    for n in range(1,m):
        if n<m:
            j=j*n
    print("{0}的阶乘是{1}".format(m,j))

if __name__ == '__main__':
    N = input("请随意输入一个数字N:")
    jiecheng(int(N))
