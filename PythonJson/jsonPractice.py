# Json is a syntax for storing and exchanging data

# Json is a text, written with JavaScript object notation

# Python has a built-in module called json to work with JSON data

# json to python
# json.loads()

# python to json
# json.dumps()

import json

x = '{"name":"John","age":"30","city":"New York"}'

# parse x:

y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["age"])


#  convert fom python to json

# use json.dumps()

x = {"name": "John", "age": 30, "city": "New York"}

y = json.dumps(x)

print(y)

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name": "John", "age": "37"}))

z = json.dumps(["apple", "banana", "cherry"])
print(type(z))
print(z)

x = json.dumps(("apple", "banana", "mango"))
print(type(x))
print(x)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

print(json.dumps(x))
print(type(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))


print(json.dumps(x, indent=4, sort_keys=True))