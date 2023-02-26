import re

def sa(s):
    return re.sub(r'(?:_+)(\w)', lambda m: m.group(1).upper(), s)
    


s = str(input())
c = sa(s)
print(c)