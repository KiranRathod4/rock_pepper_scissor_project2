import random 
print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)            "0"

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)         "1"

    _______
---'   ____)____
          ______)       "2"
       __________)
      (____)
---.__(___)\n''')

images= ["rock","pepper","scissor"]

user_choice = int(input("ek number choose kar: type 0 for rock,type 1 for paper,  type 2 for scissor:\n"))

if user_choice >=3 or user_choice <0:
    print("invalid number, choose between 0 to 2")
else:
    print(images[user_choice])
    computer_choice = random.randint(0,2)
    print("computer_choice:")
    print(images[computer_choice])
    
    if user_choice  == computer_choice:
        print("its a draw")
        
    elif computer_choice==0 and  user_choice == 2 :
        print("you lose")
        
    elif computer_choice == 2 and user_choice ==0:
        print("you win")
        
    elif user_choice > computer_choice:
        print("you win")
    
    elif user_choice <computer_choice:
        print("you lose")
   