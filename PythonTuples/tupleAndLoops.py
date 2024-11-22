thistuple = ("apple", "banana", "orange")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("Dhaka", "Chittagong", "Rangpur")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# python join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)