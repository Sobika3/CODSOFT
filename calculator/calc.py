def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while True:
    print("Please select operation -\n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n" \
            "5. Exit\n")

    select = int(input("Select operations from 1, 2, 3, 4, 5: "))

    if select == 5:
        print("Exiting...")
        break

    if select not in range(1, 5):
        print("Invalid choice. Please select a number between 1 to 4.")
        continue

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if select == 1:
        print(number_1, "+", number_2, "=", add(number_1, number_2))

    elif select == 2:
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))

    elif select == 3:
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))

    elif select == 4:
        if number_2 == 0:
            print("Error! Division by zero.")
        else:
            print(number_1, "/", number_2, "=", divide(number_1, number_2))
