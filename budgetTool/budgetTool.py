import os
import csv

def write_to_csv(file_name, data):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        
def read_from_csv(file_name):
    if not os.path.exists(file_name):
        return []

    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)

def main_menu():
    while True:
        print('1. Add an expense')
        print('2. View expenses')
        print('3. Exit')
        choice = input('Enter your choice: ')
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print('Bye!')
            break
        else:
            print('Invalid choice. Try again.')

def add_expense():
    expense_name = input('Enter expense name: ')
    expense_amount = input('Enter expense amount: ')
    write_to_csv('expenses.csv', [expense_name, expense_amount])
    print('Expense added successfully!')

def view_expenses():
    expenses = read_from_csv('expenses.csv')
    for expense in expenses:
        print('Expense name: {}\tExpense amount: {}'.format(expense[0], expense[1]))

if __name__ == '__main__':
    main_menu()
