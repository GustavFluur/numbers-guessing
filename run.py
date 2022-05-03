number = 10 
print('Try to guess the number (between 0 and 50) in three guesses!')

try1 = int(input('\Enter your first guess: '))
if try1 == number:
    print('On the first try you scored the right one, what is your secret!?')
elif try1 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, number to low!')

try2 = int(input('\Enter your second guess: '))

if try2 == number:
    print('On the first try you scored the right one, what is your secret!?')
elif try2 > number:
    print('Your guess is too high, please try again!')
else: 
    print('Almost there, number to low!')
    
try3 = int(input('\Enter your third guess: '))
