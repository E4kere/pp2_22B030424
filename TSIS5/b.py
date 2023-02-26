import re

n = r'a(b){2,3}'

s = str(input())

m = re.search(n, s)

if m:
    print(m.group(), m.start())
else: 
    print("NO")