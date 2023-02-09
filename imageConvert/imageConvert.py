from PIL import Image

def convert_image(input_path, output_path):
    image = Image.open(input_path)
    image.save(output_path)

input_path = input("Enter the path of the image you want to convert: ")
output_path = input("Enter the path where you want to save the new image: ")

convert_image(input_path, output_path)

print("Image converted successfully!")
