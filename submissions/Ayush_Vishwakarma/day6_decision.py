choice = str(input("Choose a path (left or right)")).lower()
if choice == 'left':
    print("You found a hidden tunnel! You’re safe.")
elif choice == 'right':
    print("Oh no! The Glitch’s trap was here! Try again.")
else :
    print("Invalid choice. Please enter 'left' or 'right'.")