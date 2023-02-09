import random

def roll_dice(num_sides, num_dice):
    result = []
    for i in range(num_dice):
        result.append(random.randint(1, num_sides))
    return result
if __name__ == "__main__":
    while True:
        num_sides = int(input("How many sides should each die have? "))
        num_dice = int(input("How many dice would you like to roll? "))
        result = roll_dice(num_sides, num_dice)
        print("You rolled:", result)
        user_input = input("Roll again? (y/n) ")
        if user_input.lower() != "y":
            break
