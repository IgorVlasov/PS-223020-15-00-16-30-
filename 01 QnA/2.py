# num = int(input())
# j = 0
# ent = False
# n = 0
# if num > 5000 and num < 10000:
# 	num = str(num)
# 	for i in num:
# 		j += 1
# 		if j == 1:
# 			n = i
# 		if j > 2:
# 			if j == 3 and i != '0':
# 				f_1 = int(i)
# 			if j == 4 and i != '0':
# 				f_2 = int(i)
# 				ent = True

# num = int(num)

# if ent == True:
# 	print (f_1 , f_2)
# 	c = num - ((f_1**2) * (f_2**2))
# elif ent == False:
# 	c = num - n**2
# print(c)





num = int(input())

n1 = num//1000
n2 = num//10%10
n3 = num%10
print(n1,n2,n3)

if n2*n3!=0 :
	num-=(n2*2)*(n3**2)
else:
	num-=n1**2
print(num)



