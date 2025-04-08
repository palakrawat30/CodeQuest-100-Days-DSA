#Ask the user to choose a path (left or right).
#If they choose ‘left’, print: "You found a hidden tunnel! You’re safe. 🚀"
#If they choose ‘right’, print: "Oh no! The Glitch’s trap was here! Try again. 😨"
#If they enter something else, print: "Invalid choice. Please enter 'left' or 'right'."
path=input("Choose a path : ").lower()
if path=="left":
    print("You found a hidden tunnel ! You’re safe. 🚀")
elif path =="right":
    print("Oh no! The Glitch’s trap was here! Try again. 😨")  
else:
    print("Invalid choice. Please enter 'left' or 'right") 
