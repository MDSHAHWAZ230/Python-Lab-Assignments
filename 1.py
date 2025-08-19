# Write a program to create a calculator 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Select operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
operation = input("Enter operation (1/2/3/4): ")

if operation == '1':
    result = a + b
    print(f"The result of addition is: {result}")

elif operation == '2':
    result = a - b
    print(f"The result of subtraction is: {result}")

elif operation == '3':
    result = a * b
    print(f"The result of multiplication is: {result}")

elif operation == '4':
    if b != 0:
        result = a / b
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected. Please choose a valid operation (1/2/3/4).")