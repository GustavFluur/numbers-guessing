import sys
import random

number = random.randint(1, 100)
print('Try to guess the number (between 1 and 100) on three guesses!')

"""Here the user is typing in the number and to succeed in this game, you must choose the right one. How you are doing that is by selecting a number between 0 - 20."""

try1 = int(input('\Enter your first guess: '))
if try1 == number:
    print('On the first try you scored the right one, what is your secret!?')
    sys.exit()
elif try1 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, the number too low!')

try2 = int(input('\Enter your second guess: '))

if try2 == number:
    print('Great, you made it on the second try!')
    sys.exit()
elif try2 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, the number too low!')

try3 = int(input('\Enter your third guess: '))

if try3 == number:
    print('Correct number, nice one!')
    sys.exit()
elif try3 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, the number too low!')
