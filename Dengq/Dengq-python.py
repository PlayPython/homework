# 使用循环和算术运算，生成0到20的偶数
#第一种方法
for a in range(0,21,2):
	print(a)
#第二种方法
for number in range(0,21):
	if number % 2 == 0:
	    print(number)
	    continue
# 使用循环和算术运算，生成0到20的奇数
#第一种方法
for b in range(1,21,2):
	print(b)
#第二种方法	
for number in range(1,21):
	if number % 2 == 1:
	    print(number)
	    continue
# 写一个函数，判断一个数是否被另一个数整除
#整除2
i = 99
if i % 2 == 0:
    print('%d能被2整除'%(i))
else:
    print('%d不能被2整除'%(i))
# 创建一个函数，除去字符串前面和后面的空格
x='xyz'.center(10)
x
y=x.lstrip()
y
z=x.rstrip()
z
a=x.strip()
a 
# 判断一个数字是否为素数
def isPrime(n):    
    if n <= 1:    
        return false   
    i = 2   
    while i*i <= n:    
        if n % i == 0:    
            return false  
        i += 1   
    return true
byebye