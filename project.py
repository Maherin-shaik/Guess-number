import random
def num_guessing():
    my_num=random.randint(1,50)
    chance=0
    print("*****Welcome to NUMBER GUESSING GAME*****")
    
    print("You have 3 chances try to guess number under 1 to 50 numbers:")
    while True:
        try:
            num=int(input("Enter your guess:"))
            chance+=1
            if chance==3:
                print("Your chances over...")
                print("our number is ",my_num)
                break
            elif num==my_num:
                print("contratulation your guess is correct!!!!")
                break
            elif num>my_num:
                    print("oh..its too high")
          
            else:
                    print("oh..its too low")
                
        except ValueError :
            print("Invalid number...please recheck and enter valid number.")
num_guessing()