class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"name: {self.name}, salary: {self.salary}")

# Create an Employee object with name and salary as separate arguments
emp = Employee("John", 50000)
emp.display()
