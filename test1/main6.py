n = int(input("введите число" ))
s = 1
d=0
for i in range(n):
	d+=1
	s+= 1/(d)
print(s)