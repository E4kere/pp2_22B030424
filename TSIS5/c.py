import re



e = str(input())
pattern = r"[a-z]*_[a-z]+"


matches = re.search(pattern, e)

print(matches)