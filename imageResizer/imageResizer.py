import PIL
from PIL import Image
image = Image.open("snakeSize.png")
print("Current size:", image.size)
image.thumbnail((image.size[0]//2, image.size[1]//2))
print("New size:", image.size)
image.save("your_resized_image.png")
