# Write a program to convert Celsius to Fahrenheit and vice versa 

print("Select conversion type:")
print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
conversion_type = input("Enter conversion type (1/2): ")

if conversion_type == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")

elif conversion_type == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")

else:
    print("Invalid conversion type selected. Please choose a valid option (1/2).")

# --- IGNORE ---