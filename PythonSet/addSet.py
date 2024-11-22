thisset = {"apple", "banana", "cherry"}

thisset.add("orange")  # it takes only one argument

print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical) # takes many arguments

print(thisset)


# update will modify the added data to a new set value regarding of any type

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)