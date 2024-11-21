print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])
print()

for x in "banana":
    print(x)

print()
    
a = "Hello, World!"
print(len(a))
print()

txt = "The best things in life are free!"
print("free" in txt)

print()

txt1 = "World is full of exitements"
if "exitements" in txt1:
  print("Yes, 'exitements' is present")
  
print()

txt1 = "World is full of exitements"
if "my" not in txt1:
  print("Yes, 'my' is not present")
  
print()

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")