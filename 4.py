import re

s = "AaaasvAvsd"

x = re.findall("[A-Z][a-z]", s)

print(x)