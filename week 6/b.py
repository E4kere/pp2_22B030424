import re


s = str(input())
for i in s:
    x = re.sub("^[^a-zA-Z0-9]","-",  i)
    print(x, end = "")