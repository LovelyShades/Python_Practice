# String data types

#literal assignment
first = "Dave"
last = "Gray"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor function
pizza = str("Pepypperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)