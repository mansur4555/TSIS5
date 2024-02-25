import re

s = "sA_b"

x = re.split("_", s)
o = list()
for i in x:
    if i.islower():
        o.append(i)
print(o)