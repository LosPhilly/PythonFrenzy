import sys
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Enter the name of the file: ")
file = open(filename, "r")
contents = file.read()
file.close()
while True:
    print("""
    What would you like to do?
    1. View the contents of the file
    2. Add new text to the file
    3. Quit the program
    """)

    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        print(contents)
    elif choice == "2":
        new_text = input("Enter the new text: ")
        contents += new_text
    elif choice == "3":
        break
file = open(filename, "w")
file.write(contents)
file.close()
