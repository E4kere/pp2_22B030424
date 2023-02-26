import re

n = str(input())

s = r'\b[A-Z][a-z]+'

r = re.findall(s, n)
for i in r:
    print(i)
 