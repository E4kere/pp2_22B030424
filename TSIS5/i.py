import re

def ssa(s):
   return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)


c = str(input())
s = ssa(c)
print(s)