import math

def volume_calculator(shape, *dimensions):
    if shape == "sphere":
        volume = (4/3) * math.pi * (dimensions[0]/2)**3
    elif shape == "cylinder":
        volume = math.pi * (dimensions[0]/2)**2 * dimensions[1]
    elif shape == "cone":
        volume = (math.pi * (dimensions[0]/2)**2 * dimensions[1])/3
    elif shape == "rectangular prism":
        volume = dimensions[0] * dimensions[1] * dimensions[2]
    elif shape == "cube":
        volume = dimensions[0]**3
    elif shape == "ellipsoid":
        volume = (4/3) * math.pi * dimensions[0] * dimensions[1] * dimensions[2]
    print(f"The volume of the {shape} is {volume}.")
if __name__ == "__main__":
    shape = input("What shape do you want to calculate the volume of? ")
    dimensions = [float(x) for x in input("Enter the dimensions separated by a comma: ").split(",")]
    volume_calculator(shape, *dimensions)
