def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def main():
    while True:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = bmi_calculator(weight, height)
        print("Your BMI is:", bmi)
        user_input = input("Would you like to calculate your BMI again? (y/n): ")
        if user_input == "n":
            break
        
if __name__ == "__main__":
    main()
