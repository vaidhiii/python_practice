class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def employee_details(self):
        print(f"Employee Name:{self.name}\nEmployee ID:{self.id}\nSalary:{self.salary}")


employee1 = Employee("Matt Donavan", 202607245, 500000)
employee1.employee_details()
