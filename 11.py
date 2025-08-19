# Write a program to abreviate your name without using complex codes

name = input("Enter your name: ")

abbreviated_name = ''.join(part[0].upper() for part in name.split())
print(f"Abbreviated name: {abbreviated_name}")