choice=input("Which path do you prefer?(left/right):").lower()
if choice=="left":
    print("you found a hidden tunnel!you are safe")
elif choice=="right":
    print("oh no!the glitch's trap was here!try again")
else:
    print("Invalid choice.please enter 'left' or 'right'")