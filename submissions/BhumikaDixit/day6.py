turn=input("Which path do you choose? (left/right): ")
if turn == "left" or turn == "Left" or turn == "LEFT" :
    print("You found a hidden tunnel! You're safe. 🚀")
elif turn == "right" or turn == "Right" or turn == "RIGHT" :
    print("Oh no! The Glitch's trap was here! Try again.😨")
else:
    print("Choose left/right")
