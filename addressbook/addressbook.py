address_book = []
def add_person(name, address, phone):
    person = {
        "name": name,
        "address": address,
        "phone": phone
    }
    address_book.append(person)

def get_person(name):
    for person in address_book:
        if person["name"] == name:
            return person
    return None

def main():
    while True:
        action = input("What would you like to do? (add/get/quit): ")
        if action == "add":
            name = input("Name: ")
            address = input("Address: ")
            phone = input("Phone: ")
            add_person(name, address, phone)
        elif action == "get":
            name = input("Name: ")
            person = get_person(name)
            if person:
                print("Name:", person["name"])
                print("Address:", person["address"])
                print("Phone:", person["phone"])
            else:
                print("Sorry, that person is not in the address book.")

        elif action == "quit":
            break
        
        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    main()
