import re

s = "AsatuIsTheBestDastur"
x = re.findall("[A-Z][a-z]*", s)
print(' '.join(x))