a = 5234
m = max([int(i) for i in str(a)])
n = min([int(i) for i in str(a)])
print (m, n)

if a < 10000:
  b = m
  m = n
  n = b
  print (m, n)