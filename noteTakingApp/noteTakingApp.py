import tkinter as tk
root = tk.Tk()
root.title("Note-Taking App")
root.geometry("300x300")
def save_note():
    note = note_input.get("1.0", "end-1c")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
def view_notes():
    with open("notes.txt", "r") as f:
        notes = f.read()
        view_notes = tk.Toplevel()
        view_notes.title("All Notes")
        view_notes.geometry("400x400")
        notes_label = tk.Label(view_notes, text=notes)
        notes_label.pack()
note_input = tk.Text(root, height=10, width=30)
note_input.pack()
save_button = tk.Button(root, text="Save Note", command=save_note)
save_button.pack()

view_button = tk.Button(root, text="View Notes", command=view_notes)
view_button.pack()
