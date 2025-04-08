k=input('Choose a path: Left or Right')
ch=k.lower()
if ch=="left":
    print('You found a hidden tunnel!You are Safe.')
elif ch=='right':
    print('Oh no!The Gitch trap was here!Try again.')
else:
    print9("Invalid choice.Please enter 'left' or 'right'.")
    