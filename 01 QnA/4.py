num = str(input())
j = 0 


def check (x,y,z):

	x_b = False
	y_b = False
	z_b = False

	if x % 3 :
		x_b = True 
	if y % 5 :
		y_b = True 
	if z % 10 :
		z_b = True 
	
	#  типо теперь самая веселуха
	if x_b == True and y_b == True and z_b == True:
		print(x+y+z)
	elif x_b == True:
		print("0")
	elif y_b == True :
		print("1")
	elif z_b == True:
		print("2")
	elif x_b == False and y_b == False and z_b == False:
		print("никакое из условий не выполнено")

	return 0

for i in num :
	j+=1
	if j == 1 :
		i_1 = i
		
	if j == 2 :
		i_2 = i
		
	if j == 3 :
		i_3 = i
		
	if j == 4 :
		i_4 = i


i_1=int(i_1)
i_2=int(i_2)
i_3=int(i_3)
i_4=int(i_4)

c = int(i_1*i_2)
d = int(i_2*i_3)
e = int(i_3*i_4)

check(c,d,e)