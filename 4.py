# Write a program to calculate simple interest when time, rate of interest (ROI), and principal are given  

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest (ROI): "))
t = float(input("Enter the time in years: "))

SI = (p*r*t) / 100
print(f"The simple interest is: {SI}")