num = int(input())

n1 = num//1000
n2 = num//10%10
n3 = num%10


if n2*n3!=0 :
	num-=(n2*2)*(n3**2)
else:
	num-=n1**2
print(num)



