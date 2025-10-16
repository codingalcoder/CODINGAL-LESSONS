print("welcome to elite capital banks")
while True:
    try:
        age = int(input("Enter your age: "))
        if 0 <= age <= 45:
            break
        else:
            print("Age must be between 0 and 45.")
    except ValueError:
        print("Invalid input! Please enter a number.")
print(f"you are elidgible for opening an acount")
