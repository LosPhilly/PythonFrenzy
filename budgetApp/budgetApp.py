import csv
def add_expense(amount, description):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, description])
def display_expenses():
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        expenses = [row for row in reader]

    for expense in expenses:
        print("Amount: ${} Description: {}".format(expense[0], expense[1]))
def main():
    while True:
        expense = input("Enter expense (amount and description separated by a comma): ")
        if expense == "quit":
            break
        expense = expense.split(", ")
        add_expense(expense[0], expense[1])

    display_expenses()
if __name__ == "__main__":
    main()
