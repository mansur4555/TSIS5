import re

s = "aaAabadfsb ahgjvh,"

x = re.findall(r"\ba.*b\b", s)
print(x)