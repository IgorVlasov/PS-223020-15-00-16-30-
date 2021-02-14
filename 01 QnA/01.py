x = input()
x1, x2 = x.split()
x1, x2 = int(x1), int(x2)

x = x1**(2*x2) - x2**(2*x1)

print(x)