import re


s = r'(ab*)'

n = str(input())

e = re.search(s, n)

if e: 
    print(e.group(), e.start())
else: 
    print("No")
