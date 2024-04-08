class Employee:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == "name":
                self.name = value
            elif key == "gender":
                self.gender = value
            elif key == "level":
                self.level = value

emp1 = Employee(name="Denise", gender="Female", level=1)
emp2 = Employee(gender="Male", level=1)
print(emp2.name)