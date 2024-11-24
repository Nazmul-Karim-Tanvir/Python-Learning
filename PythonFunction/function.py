def my_function():
    print("Hello from a function")


my_function()


# Arguments
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobies")
my_function("Linus")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# Arbitrary Arguments, *args


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3+" "+child2+" "+child1)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
    print("His last name is " + kid["lname"])
    
my_function(fname = "Tobias", lname = "Refsnes")

# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# passing a list as an argument

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# To let a function return a value, use the return statement:

def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass statement is used when a statement is required syntactically but you do not want any code to be executed.

def my_function():
    pass

my_function()


# positional only arguments

def my_function(a, /, b):
    print(a, b)

my_function(3, 5)
my_function(8, 9)

# Positional-Only Arguments:
def my_function(x, /):
  print(x)

my_function(3)

# Keyword-Only Arguments

def my_function(*, x):
  print(x)

my_function(x = 18)


# Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


# Recursive functions

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))