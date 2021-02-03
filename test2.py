a = 6023
s = str(a)
b = int(s[0])
c = int(s[2])
d = int(s[3])

if a > 5000:
  if a < 10000:
    if c !=0 and d !=0:
      n = a - (c**2*d**2)
      print(n)
    else: 
      g = a - (b**2)
      print(g)
      #test2