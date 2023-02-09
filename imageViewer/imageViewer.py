import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk, Image, ImageDraw


root = tk.Tk()
root.title("Image Viewer")


def select_image():
    filename = tk.filedialog.askopenfilename()
    image = Image.open(filename)
    image = image.resize((500, 500), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image

image_label = tk.Label(root)
image_label.pack()
select_image_button = tk.Button(root, text="Select Image", command=select_image)
select_image_button.pack(side="bottom")


root.mainloop()
