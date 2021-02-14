a = int(input())

a1 = a//1000
a2 = a//100%10
a3 = a//10 % 10
a4 = a%10

a12 = a1 * a2
a23 = a2 * a3
a34 = a3 * a4

if a12 % 3 == 0 and a23 % 5 == 0 and a34 % 10 == 0
print (a12 + a23 + 34)
elif a12 % 3 == 0:
  print(0)
elif a23 % 5 == 0:
  print(1)
elif a34 % 10 == 0:
  print(2)
