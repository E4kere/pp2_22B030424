import re

def ca(s):
   return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()


c = "MyCamelCaseString"
s = ca(c)
print(s)