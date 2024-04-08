## Classes

- Python's object constructor
- Two parts: attributes and methods

```python [0|1|2|2-5|7-8,10-11,13-15|17-18|2-5|20-22|23|7-8|24]
class Employee:
    def __init__(self, name, gender, level):
        self.name = name
        self.gender = gender
        self.level = level

    def promote(self):
        self.level += 1

    def demote(self):
        self.level = max(0, self.level - 1)

    def change_name(self, name):
        self.name = name
        print(f"Your new name is {name}")

# Create new instance of the Employee class
employee = Employee("Denise", "Female", 1)

print(employee.name)                # Denise
print(employee.gender)              # Female
print(employee.level)               # 1
employee.promote()
print(employee.level)               # 2
```