import tkinter as tk
import pickle
root = tk.Tk()
root.title("To-do List of Doom")
todo_list = []
selected_todo = tk.StringVar()
def save_list():
    with open("todo.pickle", "wb") as f:
        pickle.dump(todo_list, f)
def load_list():
    try:
        with open("todo.pickle", "rb") as f:
            todo_list = pickle.load(f)
    except:
        todo_list = []
def add_item():
    todo = add_entry.get()
    if todo:
        todo_list.append(todo)
        todo_listbox.insert("end", todo)
    add_entry.delete(0, "end")
def delete_item():
    selected = todo_listbox.curselection()
    if selected:
        todo_list.pop(selected[0])
        todo_listbox.delete(selected[0])
todo_listbox = tk.Listbox(root, listvariable=selected_todo)
todo_listbox.pack()

add_entry = tk.Entry(root)
add_entry.pack()

add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack()

delete_button = tk.Button(root, text="Delete", command=delete_item)
delete_button.pack()

load_list()
root.mainloop()
save_list()

