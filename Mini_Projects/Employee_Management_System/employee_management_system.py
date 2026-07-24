employees = []

# Adding employee


def add_employees(**kwargs):
    employees.append(kwargs)
    print("\nEmployee Added Successfully!\n")


# Display Employees


def display_employees():
    if len(employees) == 0:
        print("\nNo employees found.\n")
        return

    print("\n--------Employees List--------")
    for employee in employees:
        print("Name: ", employee["Name"])
        print("Salary: ", employee["Salary"])
        print("Department: ", employee["Department"])
        print("--------------------")


def search_employee(search_name):
    for employee in employees:
        if employee["Name"].lower() == search_name.lower():
            print("\nEmployee Found!")
            print("Name: ", employees["Name"])
            print("Salary: ", employees["Salary"])
            print("Department: ", employees["Department"])
    else:
        print("Employee Not Found.")


while True:
    print("--------EMPLOYEE MANAGEMENT SYSTEM--------")
    print("\n1. Add Employee\n2. Display Employee\n3. Search Employee\n4. Exit")
    choice = int(input("\nEnter what you want to do:"))
    if choice == 1:
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")
        add_employees(Name=name, Salary=salary, Department=department)
    elif choice == 2:
        display_employees()
    elif choice == 3:
        search_name = input("Enter name of Employee you want to search: ")
        search_employee(search_name)
    elif choice == 4:
        print("Exiting Employee Management System...")
        break
    else:
        print("Enter Valid Choice.")
