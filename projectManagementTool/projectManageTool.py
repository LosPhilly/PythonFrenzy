import csv
import os

def generate_data():
    data = [["Project Name", "Task", "Status"],
            ["Project A", "Task 1", "In Progress"],
            ["Project A", "Task 2", "Not Started"],
            ["Project B", "Task 1", "In Progress"],
            ["Project B", "Task 2", "In Progress"],
            ["Project B", "Task 3", "Not Started"],
            ["Project C", "Task 1", "Completed"],
            ["Project C", "Task 2", "Completed"],
            ["Project C", "Task 3", "Completed"]]
    return data
def write_to_csv(data):
    filename = "project_data.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("Data written to " + filename)
def read_from_csv():
    filename = "project_data.csv"
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data
def display_data(data):
    print("Project Management Tool\n")
    print("Project Name\tTask\t\tStatus")
    for row in data[1:]:
        print(row[0] + "\t\t" + row[1] + "\t\t" + row[2])

def main():
    data = generate_data()
    write_to_csv(data)
    data = read_from_csv()
    display_data(data)

if __name__ == "__main__":
    main()
