#Python Practice
print("Hello world")
if 5 > 2:
 print("Five is greater than two!") 
 print("Five is greater than two!") 
x = 5
y = "Hello Message"
print(x,y)

#Python tipe casting
x = str(3)
y = int(3)
z = float(3)

print(x, type(x))
print(y, type(y))
print(z, type(z))

#Python Many values to multiple variables
x,y,z = "Orange", "Banana","Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a collection of values
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

# Python output
x = "Python is awesome"
print(x)

x= "Python "
y= "is "
z= "Awesome "

print(x,y,z)
print(x+y+z)

x=5
y=10

print(x+y)

x=5
y=10
print(x+y)

# Python global variables
x = "fantastic"

def myfunc():
    global x 
    x = "Python is "+x
    print(x)
myfunc()

print(x)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)