a, b, c = map(int, input().split());

if a == 90:
    b = c = 45
    print(1)
    
elif b == 90:
    a = c = 45
    print(1)

elif c == 90:
    a = b = 45
    print(1)   

else:
  print(0)