import sys
import random

"""
This is a simple game for user to play with,
where structure is based upon on one variable with a few if statements.
-It's a simple code
-Easy to use
-No difficulties to enhance it further.
"""
"""
For the future it require a sort of score system,
where the user is getting informed on how it's going,
and create a sort of restart system, to make the game independent.
"""

MAX_TRIES = [1, 2, 3, 4, 5]


def main():
    while True:
        number = random.randint(1, 100)
        print('Try to guess the number (between 0 and 100) on five guesses!')

        for i in MAX_TRIES:
            guess(i, number)
        print('You lost the game....')
        end_game()


def guess(i, correct_number):
    try:
        try_number = int(input('Enter guess ' + str(i) + ': '))
    except ValueError:
        print ('Please enter a number!')
        guess(i, correct_number)
        return None

    if try_number == correct_number:
        print(
            'Wow, you scored on try ' + str(i) + '! How did you know!?'.upper()
        )
        print('Shuting down..')
        end_game()
    elif try_number > correct_number:
        print('Your guess is too high, please try again!')
    else:
        print('Almost there, the number too low!')


def end_game():
    print('Wanna try again?')
    print('please press either y - yes or n - no')
    user_answer = input('y/n' + "" + ":")

    if user_answer == 'y':
        main()
    elif user_answer == 'n':
        print('Goodbye!')
        sys.exit('Shutting down')
    else:
        end_game()


main()