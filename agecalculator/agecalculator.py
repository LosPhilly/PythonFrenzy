import datetime
def calculate_age(birthdate):
    today = datetime.datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
if __name__ == '__main__':
    while True:
        birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
        if birthdate_str == "quit":
            break
        birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d')
        age = calculate_age(birthdate)
        print("You are", age, "years old.")
