thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"]) 

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
print(type(thisdict))


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)