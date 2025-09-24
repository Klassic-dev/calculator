import math

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power (x^y)")
print("6. Square Root")

choice = input("Enter choice (1/2/3/4/5/6): ")

if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == '5':
        print("Result:", math.pow(num1, num2))

elif choice == '6':
    num = float(input("Enter number: "))
    if num >= 0:
        print("Result:", math.sqrt(num))
    else:
        print("Error: Cannot take square root of negative number.")
else:
    print("Invalid choice")
