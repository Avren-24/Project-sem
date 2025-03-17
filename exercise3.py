import random

random_number = random.randint(10, 20)
guess = None

while guess != random_number:
    guess = int(input("enter your guess:"))
    if guess == random_number:
        print("congratulations")
    else:
        print("try again")
