# Write a program to convert centimetres to inches and vice versa 

print ("Select conversion type:")
print ("1. Centimeters to Inches\n2. Inches to Centimeters")
conversion_type = input("Enter conversion type (1/2): ")

if conversion_type == '1':
    cm = float(input("Enter length in centimeters: "))
    inch = cm / 2.54
    print(f"{cm} cm is equal to {inch} inches")

elif conversion_type == '2':
    inch = float(input("Enter Length in inches: "))
    cm = inch * 2.54
    print (f"{inch} inches is equal to {cm} cm")

else:
    print("Invalid conversion type selected. Please choose a valid option (1/2).")

# --- IGNORE ---