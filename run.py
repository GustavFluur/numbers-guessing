number = 5 
print('Try to guess the number (between 1 and 14) in three guesses!')

try1 = int(input('\Enter your first guess: '))
if try1 == number:
    print('On the first try you scored the right one, what is your secret!?')
elif try1 > number:
    print('Your guess is too high, please try again!')
try2 = int(input('\Enter your second guess: '))
try3 = int(input('\Enter your third guess: '))
