x = input()
x1, x2, x3 = x.split()
x1, x2, x3 = int(x1), int(x2), int(x3)

print(x1, x2, x3)

if x1 + x2 + x3 != 180:
  print(0)
elif x1 == x2 and x3 == 90:
  print(1)
elif x3 == x2 and x1 == 90:
  print(1)
elif x1 == x3 and x2 == 90:
  print(1)
else:
  print(0)
