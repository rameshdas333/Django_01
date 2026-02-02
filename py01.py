class Employee:
    count = 0   # Class variable

    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience
        Employee.count += 1   # Every time an object is created, count increases

    def get_designation(self):
        if self.experience <= 2:
            return "Junior Software Developer"
        elif 2 < self.experience <= 5:
            return "Mid Senior Software Developer"
        else:
            return "Senior Software Developer"


# Creating objects
e1 = Employee(name="Nahid", salary="10000", experience=2)
e2 = Employee(name="Salman", salary="50000", experience=5)

# Print count
print(Employee.count)
