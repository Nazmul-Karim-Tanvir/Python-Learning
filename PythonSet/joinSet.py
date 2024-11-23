# union
set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

# | operator

set3 = set1| set2

print(set3)



# join multiple sets together

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
#  join a set with tuples or other data types like lists or tuples using union()

x = {"a","b","c"}
y= (1,2,3)

z = x.union(y)
print(z)

# The update() method inserts the items in set2 into set1:

set1 = {"a","b","c"}
set2 = {10,20,30}
set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

# intersection()
# Join set1 and set2, but keep only the duplicates:
set1 = {"apple","orange","mango"}
set2 = {"google","orange","whatsapp"}

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)


# The values True and 1 are considered the same value. The same goes for False and 0.


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)


# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)