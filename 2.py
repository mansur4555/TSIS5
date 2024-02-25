import re

s = "abbb"

x = re.findall("a.b{2}", s)
print(x)