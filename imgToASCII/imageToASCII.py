import png
import sys

with open("asciisnake60x60.png", "rb") as image_file:
    image = png.Reader(file=image_file).asRGBA()

    for row in image[2]:
        for pixel in range(0, len(row), 4):
            red, green, blue, alpha = row[pixel], row[pixel + 1], row[pixel + 2], row[pixel + 3]
            brightness = int((red + green + blue) / 3)
            if brightness >= 240:
                character = " "
            elif brightness >= 200:
                character = "."
            elif brightness >= 160:
                character = "*"
            elif brightness >= 120:
                character = ":"
            elif brightness >= 80:
                character = "o"
            elif brightness >= 40:
                character = "&"
            else:
                character = "#"
            print(character, end="")
        print()

sys.exit()
