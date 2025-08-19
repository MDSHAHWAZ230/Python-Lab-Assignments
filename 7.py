# Write a program to convert KG to Pound and vice versa.

print("Select conversion type:")
print("1. KG to Pound\n2. Pound to KG")
conversion_type = input("Enter conversion type (1/2): ")

if conversion_type == '1':
    kg = float(input("Enter weight in KG: "))
    pound = kg * 2.20462
    print(f"{kg} KG is equal to {pound} Pound")

elif conversion_type == '2':
    pound = float(input("Enter weight in Pound: "))
    kg = pound / 2.20462
    print(f"{pound} Pound is equal to {kg} KG")

else:
    print("Invalid conversion type selected. Please choose a valid option (1/2).")

# --- IGNORE ---