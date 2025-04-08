choice = input("Which path do you choose? (left/right): ") # get the choice from the user
if(choice.lower() == "left"): # if the condition is true, if block executes, otherwise the control flow goes to the elif block
    print("You found a hidden tunnel! You're safe 🚀")
elif(choice.lower() == "right"): # if the 'if' condition fails, the control flow come to elif. If the condition is true, elif block executes, otherwise it goes to else block
    print("Oh no! The Glitch's trap was here! Try again 😨")
else: # if the above two conditions fails, else block gets executed
    print("Invalid choice. Please enter 'left' or 'right'")
