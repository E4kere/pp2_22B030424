import re

n = str(input())
t = r'\b\d{2}/\d{2}/\d{4}'
dates = re.findall(t, n)
for date in dates:
    print(date, end = " ")