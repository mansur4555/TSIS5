import re

s = "PythonIsSimple"

print(re.findall("[A-Z][^A-Z]*", s))