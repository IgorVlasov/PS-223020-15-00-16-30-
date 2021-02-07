a, b, c = map(int, input().split())

def check(x,y,z):
	if x == 90:
		if y==z:
			print("1")
	

if a + b + c == 180:
	if a == b or b == c or a == c:
		if a > b and a > c :
			check(a,b,c)
		if b > a and b > c : 
			check(b,a,c)
		else:
			check(c,a,b)

else :
	print ("0")