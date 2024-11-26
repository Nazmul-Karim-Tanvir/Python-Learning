import re

txt = "10+ I love to watch rain drops"

# Find all occurrences of the word "rain"
x = re.findall("[arn]", txt)
print(x)

x = re.findall("[^arn]", txt)
print(x)


x = re.findall("[a-z]", txt)
print(x)

x = re.findall("^[a-z]", txt)
print(x)

x = re.findall("[0123]", txt)
print(x)

x = re.findall("[0-9]", txt)
print(x)

x = re.findall("[0-9][0-9]", txt)
print(x)

x = re.findall("[a-zA-Z]", txt)
print(x)

x = re.findall("[+]", txt)
print(x)