import re

s = "ab"

x = re.findall("a.*b", s)
print(x)