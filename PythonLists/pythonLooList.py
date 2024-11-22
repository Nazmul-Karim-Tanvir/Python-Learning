thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)
    
# Print all items by referring to their index number:

for i in range(len(thislist)):
    print(thislist[i])
    
# while loop
thisnewlist = ["tom","and","jerry"]

i=0
while i<len(thisnewlist):
    print(thisnewlist[i])
    i=i+1
    
# A short hand for loop that will print all items in a list:

thislist = ["mango", "banana", "cherry"]
[print(x) for x in thislist]
