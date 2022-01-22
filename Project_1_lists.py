"""
The program will
1. display a list 
2. have a user choice and index position and an input value 
3. replace value with index position with user chosen input value 
"""


game_list = ['m', 'o', 'h']


def game_display(game_list):
    print("This is your current list")
    print(game_list)


def position_choice():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice = input("Enter a position to replace (0,1,2): ")
        if choice not in ['0', '1', '2']:
            print("Invalid input choose a valid choice(0,1,2)")
    return int(choice)


def replacement_choice(game_list, poition):
    user_placement = input("Enter string to replace at poistion: ")
    game_list[poition] = user_placement
    return(game_list)


def game_on_choice():

    choice = 'wrong'

    while choice not in ['y', 'n', 'N', 'Y']:
        choice = input("Do you want to play again? (Y,N): ")
        if choice not in ['y', 'n', 'N', 'Y']:
            print("Sorry!, I didn't understand, chose Y or N: ")

    if choice == 'Y':
        return True
    else:
        return False


game_on = True

while game_on:
    game_display(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    game_display(game_list)

    game_on = game_on_choice()
