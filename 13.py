# Write a program to add all the elements in a list

a = input("Enter a list of numbers separated by commas: ").split(',')
nums = [float(num) for num in a]
total = sum(nums)
print("The sum of the numbers is:", total)
# --- IGNORE ---