import random

secret_number = random.randint(1, 100)
tries, guess = 0, 0
while guess != secret_number:
    guess = int(input("Guess a number (<100): "))
    if guess > secret_number:
        print("The actual number is lower than your guessed number!!")
    elif guess < secret_number:
        print("The actual number is higher than your guessed number!!")
    tries += 1

print('You guessed it! The number was {} in {} tries'.format(guess, tries))
