
import random 

emojis={'r':'🪨','p':'📄','s':'✂'}
choices=('r','p','s')

while True:
    user_choice=input("Rock or paper or scissior ? (r/p/s): ").lower()
    if user_choice not in choices:
            print("Invalid choice!")
            continue
    computer_choice=random.choice(choices)

    print(f'you chose {emojis[user_choice]}')
    print(f'computer chose {emojis[computer_choice]}')

    if user_choice==computer_choice:
            print("Tie")
    elif (
            user_choice==("r" and computer_choice=='s') or 
            user_choice==("s" and computer_choice=='p') or 
            user_choice==("p" and computer_choice=='r')):
            print("you wins")
    else:
            print("you lose")

    
    should_continue=input("Continue? (y/n): ").lower()
    if should_continue=='n':
        break



    
