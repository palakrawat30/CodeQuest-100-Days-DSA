choice=input("Which part do you choose?(left/right): ")

if(choice=='left'or choice=='Left'or choice=='LEFT'):
    print("You found a hidden tunnel! You're safe.")

elif(choice=='right'or choice=='Right' or choice=='RIGHT'):
    print("Oh no! The Glitch's trap was here! Try again")
    
else:
    print("Invalid choice. Please enter 'left' or 'right'")