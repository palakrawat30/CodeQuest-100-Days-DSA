# Ask the user to choose a path
choice = input("Choose a path: left or right? ").lower() # lower is used to convert input into lower alphabets
# so that user is comfertable with both capital or lower alphabets

if choice == "left":
    print("You found a hidden tunnel! You’re safe. ")
elif choice == "right":
    print("Oh no! The Glitch’s trap was here! Try again. ")
else:
    print("Invalid choice. Please enter 'left' or 'right'.")
