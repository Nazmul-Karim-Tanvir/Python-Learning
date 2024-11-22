# using remove
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# using discard method

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.

#  using pop
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


# using clear

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# using del delete set completely

thisset = {"apple", "banana", "cherry"}

del thisset
if 'thisset' in globals():
    print(thisset)
else:
    print("The set has been deleted.")
