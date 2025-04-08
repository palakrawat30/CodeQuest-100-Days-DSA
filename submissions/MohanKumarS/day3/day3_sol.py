name = input("Enter your name: ")  # name - variable ->used to store a value
print("Original Name: {}".format(name)) # print a Original Name using format()
print("Secret Code: {}".format(name.upper()[::-1])) # Reverse and uppercase the variable name
# Reverse -> [::-1] -> access the element from right most => syntax: name[::-1]
# upper() -> use to uppercase the character => syntax: name.upper()
# implement both in a line: name.upper()[::-1]