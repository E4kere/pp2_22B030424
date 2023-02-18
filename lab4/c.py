import math 

side = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))

b = a * side
v = a / 2 * math.tan(180/side)
s = b * v / 2
print(s)
