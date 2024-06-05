import random
n = random.randint(1, 10)
guess = 0

while guess != n:
    guess = int(input('Guess number'))
    if guess < n:
        print('Your Number is smaller')
    elif guess > n:
        print('Your Number is bigger')
    else:
        print('You guessed right')