# Write a program to find the highest and lowest element from a list

a = input("Enter a list of numbers separated by commas: ").split(',')
nums = [float(num) for num in a]
highest = max(nums)
lowest = min(nums)
print(f"The highest number is: {highest}\nThe lowest number is: {lowest}")