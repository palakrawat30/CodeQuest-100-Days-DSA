while True:
    path=input("Which path do you choose?(left/right):\n")
    if (path in ["left","LEFT","Left"]) :
        print("You found a hidden tunnel! You're safe.")
        break
    elif path in ["right","RIGHT","Right"] :
        print("Oh no! The Glitch's trap was here! Try again.")
        break
    else :
        print("Invalid choice.Please enter left or right")
        
