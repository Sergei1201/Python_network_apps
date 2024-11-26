import random

while True:

    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input(
            f'Enter your choice from rock, paper or scissors: ').lower()

    print(f'Computer choice is {computer}')
    print(f'Your choice is {player}')

    if player == 'rock':
        if computer == 'rock':
            print('Draw!')
        if computer == 'paper':
            print('You win!')
        if computer == 'scissors':
            print('You lose!')
    elif player == 'scissors':
        match computer:
            case 'scissors':
                print('Draw!')
            case 'paper':
                print('You win!')
            case 'rock':
                print('You lose!')
    elif player == 'paper':
        match computer:
            case 'paper':
                print('Draw!')
            case 'scissors':
                print('You lose!')
            case 'rock':
                print('You win!')
    playAgain = input(f'Would you like to play again? y/n ').lower()
    if playAgain != 'y':
        break
print('Bye')
