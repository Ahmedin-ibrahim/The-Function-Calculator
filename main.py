
# Calculator using functions

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    return a / b


# Display calculator menu
print("===== SIMPLE CALCULATOR =====")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")


# Ask the user to choose an operation
choice = input("Choose an operation (1-4): ")

try:
    # Ask the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation
    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        print("Result:", divide(num1, num2))

    else:
        print("Invalid choice! Please choose between 1 and 4.")

# Handle invalid number input
except ValueError:
    print("Error: Please enter valid numbers.")

# Handle division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
