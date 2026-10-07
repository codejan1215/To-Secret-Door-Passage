import random

random = random.randint(1, 20)
guess = None
attempts = 3

while guess != random and attempts > 0:
    guess = int(input("Guess a number between 1 and 20: "))
    
    if guess < random:
        print(f"Too low! Try again. You have {attempts - 1} attempts left.")
        attempts -= 1
    elif guess > random:
        print(f"Too high! Try again. You have {attempts - 1} attempts left.")
        attempts -= 1
    else:
        print("Congratulations! You've guessed the random number:", random)

if attempts == 0:
    print("Sorry, you've run out of attempts. The random number was:", random)