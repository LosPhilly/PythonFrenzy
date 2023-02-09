import math

def area_calculator(shape, *dimensions):
    if shape == "circle":
        area = math.pi * (dimensions[0]/2)**2
    elif shape == "rectangle":
        area = dimensions[0] * dimensions[1]
    elif shape == "triangle":
        area = (dimensions[0] * dimensions[1])/2
    elif shape == "square":
        area = dimensions[0]**2
    elif shape == "parallelogram":
        area = dimensions[0] * dimensions[1]
    elif shape == "trapezoid":
        area = ((dimensions[0] + dimensions[2]) * dimensions[1])/2
    return f"The area of the {shape} is {area}."

if __name__ == "__main__":
    while True:
        shape = input("Enter the name of the shape: ")
        dimensions = [float(x) for x in input("Enter the dimensions (separated by a space): ").split()]
        result = area_calculator(shape, *dimensions)
        print(result)
        user_input = input("Do you want to calculate the area of another shape? (y/n)")
        if user_input.lower() == "n":
            print("Thank you for using the Area Calculator. Have a great day!")
            break
