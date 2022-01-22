# function interactions

from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = " "
    while guess not in [0, 1, 2]:
        guess = int(input("Pic a number 0,1,2 : "))
    return guess


def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Correct guess!")
        print(mylist)
    else:
        print("Try again ")
        print(mylist)


# Initial list
mylist = ["O", " ", " "]

# shuffle list
mixed_list = shuffle_list(mylist)

# user guess
guess = player_guess()

# check guess
check_guess(mixed_list, guess)
