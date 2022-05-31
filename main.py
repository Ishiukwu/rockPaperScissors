import random


print('''
Rules of the game:

     Rock beats Scissors
     Scissors beats Paper
     Paper beats Rock
    
    '''
      )

print("Starting Game Now...")
is_true = True
while is_true:
    beast = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(beast)
    try:
        user_input = int(input('Enter a number(0 for Rock ,1 for Paper, 2 for Scissors) '))
        user_choice = beast[user_input]
        print
        if user_choice == computer_choice:
            print('Draw')
            new_game = input("Do you want to play again?(y/n) ").lower()
            if new_game == 'y':
                continue
            else:
                break
        elif user_choice == 'Rock':
            if computer_choice == 'Scissors':
                print(f'Player({user_choice}) : CPU({computer_choice})')
                print("You win!")
            else:
                print(f'Player({user_choice}) : CPU({computer_choice})')
                print("Sorry, you lose")
        elif user_choice == 'Paper':
            if computer_choice == 'Rock':
                print(f'Player({user_choice}) : CPU({computer_choice})')
                print("You win!")
            else:
                print(f'Player({user_choice}) : CPU({computer_choice})')
                print("Sorry, you lose")
        elif user_choice == 'Scissors':
            if computer_choice == 'Paper':
                print(f'Player({user_choice}) : CPU({computer_choice})')
                print("You win!")
            else:
                print(f'Player({user_choice}) : CPU({computer_choice})')
                print("Sorry, you lose")
        break

    except:
        print("You did not enter a correct number. Please try again")
        pass

    
