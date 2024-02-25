import re

s = "Astana_is_a_capital_of_great_Britan"

x = re.split("_", s)

out = x[0] + ''.join(word.capitalize() for word in x[1:])

print(out)