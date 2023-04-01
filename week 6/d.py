import re

t = str(input())

n = r'\b^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z]+\.{1}[a-zA-Z]{2,3}$'
e = re.findall(n, t)

for g in e:
    if g:
        print("True")
    else:
        print("False")