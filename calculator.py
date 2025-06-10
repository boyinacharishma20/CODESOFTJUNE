print("Select operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {a + b}")
        elif choice == '2':
            print(f"Result: {a - b}")
        elif choice == '3':
            print(f"Result: {a * b}")
        elif choice == '4':
            if b == 0:
                print("Error! Division by zero.")
            else:
                print(f"Result: {a / b}")
    else:
        print("Invalid choice.")

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != 'yes':
        break
