a = int(input()) 
b = int(input())
c = int(input())



def check(x,y,z):
	n=y**2+z**2
	if x == n:
		print("1")
	else :
		print("0")
	return 0

if a == b or b == c or a == c:
	if a > b or a > c :
		check(a,b,c)
	if b > a or b > c : 
		check(b,a,c)
	else:
		check(c,a,b)

else :
	print ("0")