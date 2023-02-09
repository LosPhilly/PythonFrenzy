import random

insults = [
    "Are you even trying?",
    "Wow, you couldn't calculate your way out of a paper bag.",
    "I've seen better math from a toddler.",
    "You're making my processor overheat with that kind of calculation.",
    "I can calculate circles around you, and I'm a machine.",
    "I'm starting to think you're doing this on purpose.",
    "I'm pretty sure even a calculator app on a toaster could do better."
]

def calculate(operation):
    if operation == "+":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = num1 + num2
    elif operation == "-":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = num1 - num2
    elif operation == "*":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = num1 * num2
    elif operation == "/":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = num1 / num2
    elif operation == "^":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter the power: "))
        result = num1 ** num2
    elif operation == "eval":
        expr = input("Enter the expression: ")
        result = eval(expr)
    else:
        result = None
    return result



def main():
    while True:
        operation = input("Enter an operation (+, -, *, /, ^, eval): ")
        result = calculate(operation)
        if result is None:
            print(random.choice(insults))
        else:
            print("The result is:", result)
            print(random.choice(insults))

if __name__ == '__main__':
    main()
