# Define a dictionary of conversion factors
conversion_factors = {
    "inches-to-centimeters": 2.54,
    "pounds-to-kilograms": 0.453592,
    "feet-to-meters": 0.3048,
    "miles-to-kilometers": 1.60934
}

# Define a function to convert units
def convert_units(value, unit_from, unit_to):
    factor = conversion_factors[f"{unit_from}-to-{unit_to}"]
    return value * factor

# Define a function to handle user input
def main():
    value = float(input("Enter a value to convert: "))
    unit_from = input("Enter the unit to convert from (inches, pounds, feet, miles): ")
    unit_to = input("Enter the unit to convert to (centimeters, kilograms, meters, kilometers): ")
    
    result = convert_units(value, unit_from, unit_to)
    print(f"{value} {unit_from} is equal to {result} {unit_to}.")

# Call the main function
if __name__ == "__main__":
    main()
