a = 1
n = 3
b = 0
while(a<=n): 
  b = b + 1 / a  
  a = a + 1

n = 9
b = 0
for a in range(1, n + 1):
  b = b + 1 / a

print('{}\{}'.format(n,b))
# test6