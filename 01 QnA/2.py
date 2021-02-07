num = int(input())
j = 0
ent = False
n = 0
if num > 5000 and num < 10000:
	num = str(num)
	for i in num:
		j += 1
		if j == 1:
			n = i
		if j > 2:
			if j == 3 and i != "0":
				f_1 = int(i)
			if j == 4 and i != 0:
				f_2 = int(i)
				ent = True

num = int(num)

if ent == True:
	print (f_1 , f_2)
	c = num - ((f_1**2) * (f_2**2))
elif ent == False:
	c = num - n**2
print(c)
