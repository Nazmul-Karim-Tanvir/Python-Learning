x = ("apple", "banana", "cherry")
y = list(x)
print (y)
y[1] = "kewi"
print(y)
print(x)
x = tuple(y)
print(x)

# adding item to a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print (thistuple)

# adding tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("lichi",)
thistuple += y
      
print(thistuple)

# removing in tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists