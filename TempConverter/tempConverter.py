def temperature_converter():
    print("Welcome to the temperature converter!")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Please select an option: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("Temperature in Celsius:", celsius)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    temperature_converter()
