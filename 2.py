a = int(input())
j = 0
if a > 5000 and a < 10000:
	a = str(a)
	for i in a:
		j += 1
		if j == 1:
			n = int(i)
		if j > 2:
			if j == 3 and i != 0:
				f_1 = int(i)
				ent = True
			if j == 4 and i != 0 and ent == True:
				f_2 = int(i)

a = int(a)

if ent == True:
	c = a - (f_1**2) * (f_2**2)
else:
	c = a - n**2
print(c)
