# Write a program to find the area of a triangle 

print ("Select operation:")
print ("1. Area of Triangle by base and height\n2. Area of Triangle by three sides")

operation = input("Enter operation (1/2): ")

if operation == '1':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

elif operation == '2':
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    
    # Using Heron's formula to calculate area
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"The area of the triangle is: {area}")