# ①使用循环和算数运算，生成0到20的偶数
for a in range(0, 20, 2):
    print(a)

# ②使用循环和算数运算，生成0到20的奇数

for b in range(1, 21, 2):
    print(b)
# ③写一个函数，判断一个数是否被另外一个函数整除
# 例：3
# 能被某一个数整除
    x = 1008
if x % 3 == 0:
    print("%d 能被3整除" % (x))
else:
    print("%d 不能被3整除" % (x))

# 能被3整除


# ④生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围分别为（1 < N <= 100）和（0 <= n <= 2 ** 31 - 1）。然后再随机从这个列表中取N（1 <= N <= 100）个
# 随机数出来，对它们排序，然后显示这个子集。
def trandom():
    list = []
    N = random.randint(1, 101)
    for item in range(N):
        tmp = random.randint(1, 2 ** 31 - 1)
        list.append(tmp)
    print(list)
    list.sort()


if __name__ == '__main__':
    trandom()
