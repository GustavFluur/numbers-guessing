import sys
import random
"""
This is a simple game for user to play with, 
where structure is based upon on one variable with a few if statements.
"""
number = random.randint(1, 12)
print('Try to guess the number (between 0 and 12) on five guesses!')

try1 = int(input('Enter your first guess: '))
if try1 == number:
    print('Wow, you scored on the first try! How did you know!?'.upper())
    sys.exit()
elif try1 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, the number too low!')

try2 = int(input('Enter your second guess: '))

if try2 == number:
    print('Great, you made it on the second try!'.upper())
    sys.exit()
elif try2 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, the number too low!')

try3 = int(input('Enter your third guess: '))

if try3 == number:
    print('Correct number after three guesses, nice one!')
    sys.exit()
elif try3 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, the number too low!')

try4 = int(input('Enter your fourth guess: '))

if try4 == number:
    print('Correct number on the last try, well done!')
    sys.exit()
elif try4 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, the number too low!')

try5 = int(input('Enter your fifth guess: '))

if try5 == number:
    print('You made it eventually, great work!')
    sys.exit()
elif try5 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, the number too low!')