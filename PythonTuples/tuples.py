mytuple = ("apple", "banana", "cherry")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = "apple"
print(type(thistuple))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)
