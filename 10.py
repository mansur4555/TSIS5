import re

s = "AsatuIsTheBestDastur"
x = re.findall("[A-Z][a-z]*", s)
for i in range(len(x)):
    x[i] = x[i].lower()

print('_'.join(x))