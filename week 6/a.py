import re 

s = str(input())
t = False
for i in s:
    if s.isdigit():
        t = True
        break     
       
if t:
      print("Yes!")
else:
     print("No!")