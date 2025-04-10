"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:Number of vowels: 5"
"""
no_vowels = 0
s = input("\nEnter string: ")
vowels = ['a','e','i','o','u']
for i in s:
    if i in vowels:
        no_vowels+=1
print(f"Number of vowels: {no_vowels}")        