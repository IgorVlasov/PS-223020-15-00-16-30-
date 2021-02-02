a = 3352
s = str(a)
b = int(s[0])
c = int(s[1])
d = int(s[2])
f = int(s[3])

if a < 10000:
  n = b*c
  h = c*d
  j = d*f
  if n % 3 == 0:
    print(0)
    if h % 5 == 0:
      print(1) 
      if j % 10 == 0:
        print(2)
        l = n + h + j
        print(l)
 