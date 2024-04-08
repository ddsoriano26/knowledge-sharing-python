## Using Functions

```python[0|1|2|3|5-6|8-12|10,12|14-15|14]
def age_in_10_years(age):
    age += 10
    return age

def old():
    print("You are old")

def main():
    x = input("Enter your age: ")
    old_age = age_in_10_years(int(x))
    print(f"Your age in 10 years will be {old_age}")
    old()

if __name__ == '__main__':
    main()
```