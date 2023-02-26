import re

def splite(string):
    return re.findall('[A-Z][^A-Z]*', string)

string = str(input())
result = splite(string)
print(result)