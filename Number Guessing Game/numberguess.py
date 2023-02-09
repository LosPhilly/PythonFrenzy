import random

random_number = random.randint(1, 100)
print("Welcome to the number guessing game!")
print("I've chosen a number between 1 and 100, can you guess it?")
guess = int(input("Your guess: "))
if guess == random_number:
    print("Wow, you're amazing! You got it right on the first try.")
else:
    print("Sorry, that's not it. Keep guessing.")
while guess != random_number:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("Wow, you're amazing! You got it right.")
    elif guess < random_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
        
print("Congratulations, you've won! The number was", random_number)
