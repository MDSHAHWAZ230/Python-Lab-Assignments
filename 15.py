# Write a program to find the vowels from a given string

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
found_vowels = [char for char in s if char in vowels]
if found_vowels:
    print("Vowels found in the string:", ', '.join(found_vowels))