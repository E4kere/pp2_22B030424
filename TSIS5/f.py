import re

n = str(input())
for i in n:
    r = re.sub(r'^ (.) + (,) \s', ":", i)
    print(r, end = "")