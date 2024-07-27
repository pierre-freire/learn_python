import random

def user_guess(x):
    guess = 0
    random_number = random.randint(1, x)
    
    while (guess != random_number):
        guess = int(input(f'guess a number between 1 and {x}: '))
        if(guess < random_number):
            print('Sorry, guess again! too low')
        if(guess > random_number):
            print('Sorry, guess again! too high')
    print('Congrats! you have guessed the number!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)').lower()
        
        if(feedback == 'h'):
            high = guess - 1
        if(feedback == 'l'):
            low = guess + 1
    
    print(f'Congrats! the computer have guessed the number {guess}!')
    


computer_guess(10000)