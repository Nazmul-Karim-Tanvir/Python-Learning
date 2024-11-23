thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = thisdict["model"]
print(x)

x = thisdict.get("brand")
print(x)

# get keys

x = thisdict.keys()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x)

car["color"] ="white"
print(x)

# get values

x = thisdict.values()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x)

car["year"] = 2000

print(x)


# new item values

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

# get items 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


# esits cheking
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")