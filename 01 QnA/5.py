num = input()
j = 1


def check(x,y,z,w):
	if x!=y and x!=z and x!=w and y!=z and y!=w and z!=w:
		slove(x,y,z,w)
	else:
		print("задача успешно провалена")
def maxInt(x,y,z,w):
	if x>y and x>z and x>w:
		maxInt(x,y,z,w)


def minInt(i1,i2,i3,i4):
	if i2<i3 and i2<i4:
		sum(i2,i1,i3,i4)
	elif 

sum(n1,n2,n3,n4):
	n1=str(n1)
	n2=str(n2)
	n3=str(n3)
	n4=str(n4)
	print(n1+n2=n3+n4)


for i in num:
	if j == 1:
		n1=int(i)
	elif j == 2:
		n2=int(i)
	elif j == 3:
		n3=int(i)
	elif j == 4:
		n4=int(i)
	j+=1

