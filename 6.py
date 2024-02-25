import re

s = "alfn,afkl"

x = re.sub("[ ,.]", ":", s)

print(x)