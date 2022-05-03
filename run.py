number = 10 
print('Try to guess the number (between 0 and 100) in three guesses!')

"""
Here the user is typing in the number and to succeed in this game, you must choose the right one.
How you are doing that is by selecting a number between 0 - 100 for creating some challenge to the player. 
Once you type into a number you reccieve a message into the terminal or the game to understand if you are on the right path.
"""
try1 = int(input('\Enter your first guess: '))
if try1 == number:
    print('On the first try you scored the right one, what is your secret!?')
elif try1 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, number to low!')

try2 = int(input('\Enter your second guess: '))

if try2 == number:
    print('Great, you made it on the second try!')
elif try2 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, number to low!')

try3 = int(input('\Enter your third guess: '))

if try3 == number:
    print('Great, you made it on the second try!')
elif try3 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, number to low!')
