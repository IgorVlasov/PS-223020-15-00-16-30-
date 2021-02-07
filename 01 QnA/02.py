a = int( input() )
a1 = a//1000
a2 = a//100%10
a3 = a//10 % 10
a4 = a%10

if a3 != 0 and a4 !=0: # a3 * a4 !=0
  a = a - ( a3**2 * a4**2 )
  print(a)
else:
  a = a - a1 ** 2
  print(a)
