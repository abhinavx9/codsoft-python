#simple calculator
def add(x, y):
    return x+y 

def subtraction(x, y)
    return x-y

def multiply(x, y)
    return x*y

def divide(x, y)
    if y == 0:
        return "Error! Division by Zero"
    return x/y

def calculator():
    print("welcome to the arithmetic Calculator!")
    print("Select an Operator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quite: ")
        if choice == 'q':
            print("Exiting the calculator. Goodbey!")
            break

        if choice in ['1','2','3','4']:
            try:
                num1 = float(input("Enter first number"))
                num2 = float(input("Enter second number"))
            except ValueError:
                print("Invalid input! Please enter nrmbers.")
                continue

            if choice == '1':
                print(f"{num1}+{num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()