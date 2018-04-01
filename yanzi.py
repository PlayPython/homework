def fun(n):
	a=[]
	b=[]
	for i in range(n+1):
		if i%2==0:
			a.append(i)
		else:
			b.append(i)
	return a,b

fun(20)
