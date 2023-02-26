import re

n = r'a[a-z](b)'

s = str(input())

m = re.search(n, s)

if m:
    print(m.group(), m.start())
else: 
    print("NO")