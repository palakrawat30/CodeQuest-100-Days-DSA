p=0
while(p==0):
    a=input("Which path do you choose:")
    c=a.lower()
    if(c=="left"):
        print("You found a hidden tunnel!You're safe.")
        p=1
    
    elif(c=="right"):
        print("Oh no!The Glitch's trap was here!Try again.")
        p=1
    else:
        print("Invalid choise.Please enter 'left' or 'right' ")
        
