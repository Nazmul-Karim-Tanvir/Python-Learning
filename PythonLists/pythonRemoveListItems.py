# remove
# pop
# del
# clear

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# del without index will delete all including the list itself
thislist = ["apple", "banana", "cherry"]
del thislist

# clear without index will delete all excluding the list itself
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)