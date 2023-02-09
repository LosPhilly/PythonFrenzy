import tkinter as tk
import webbrowser

def open_website():
    webbrowser.open_new(entry.get())
    
root = tk.Tk()
root.title("Python's Finest Browser")

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Go", command=open_website)
button.pack()

root.mainloop()



