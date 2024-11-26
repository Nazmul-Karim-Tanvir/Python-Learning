import re

txt = "The rain in Spain"

# Check if the string starts with "The":

x = re.findall("\AThe", txt)
print(x)

if x:
    print("Yes, the string starts with 'The'")
else:
    print("No, the string does not start with 'The'")


txt = "The rain in Spain"

# Check if "rain" is present at the beginning of a WORD:

x = re.findall(r"\brain", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


txt = "The rain in Spain"

# Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



txt = "The rain in Spain 100"

# Check if the string contains any digits(numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
    

txt = "Th rain in Spain"

# return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
    
    
txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
  
  
txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
txt = "1 The rain in_Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


txt = "1 The rain in Spain ?"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
  
txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")