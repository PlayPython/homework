def jishu(a):
	for i in range(a):
		if i%2==0:
			print(i)

def oushu(a):
	for i in range(a):
		if i%2==1:
			print(i)

def zhengchu(a,b):
	if a%b==0:
		print("ok")
	else:
		print("error")

def suijishu():
	a=[]
	for i in range(random.randrange(1,101,1)):
		c=a.append(random.randrange(0,2**31,1))
d=sorted(c)
	print(d)


 def fun(a):
	if a>9:
		b=str(a)
		c=int(b[0])
		d=int(b[1])
		e=[1,2,3,4,5,6,7,8,9]
		f=["one","two","three","four","five","six","seven","eight","nine"]
		s1=f[e.index(c)]
		s2=f[e.index(d)]
		s=s1+"-"+s2
		print(s)
	else:
		e=[1,2,3,4,5,6,7,8,9]
		f=["one","two","three","four","five","six","seven","eight","nine"]
		s1=f[e.index(a)]
		print(s1)
