n=input("Enter your password: ")
upper = lower = digit = special = False
for i in n:
    if i.isupper():
        upper = True
    elif i.islower():
        lower = True
    elif i.isdigit():
        digit = True
    elif not i.isalnum():
        special = True
    
if (upper and lower and digit and special):
    print("Strong Password")
else:
    print("Weak Password", end=" (")
    if not upper:
        print("Missing uppercase latter", end=",")
    if not lower:
        print("Missing lowercase latter", end=",")
    if not digit:
        print("Missing number", end=",")
    if not special:
        print("Missing special character", end=")")