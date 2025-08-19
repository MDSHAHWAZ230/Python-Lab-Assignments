# Write a program to calculate compound interest when duration is provided 

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest (ROI): "))
t = float(input("Enter the time in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

compound_interest = p * ((1 + (r / (n * 100))) ** (n * t)) - p
print(f"The compound interest is: {compound_interest}")
