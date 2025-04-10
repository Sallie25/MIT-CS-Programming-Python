"""Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
# bob_occurrence = s.count("bob")
# print(bob_occurrence)

# count = 0
# while True:
#     bob = s.find("bob")
#     if bob == -1:
#         break
#     else:
#         count+=1
#         bob = s.find("bob",bob + 1)
#        

s = "azcbobobegghakl"
count = 0
start = 0  # Variable to track search position

while True:
    bob = s.find("bob", start)  # Find 'bob' starting from 'start'
    if bob == -1:  # If 'bob' is not found, break
        break
    else:
        count += 1
        start = bob + 1  # Move start index forward to allow overlapping matches


print("Number of times bob occurs is: " + str(count))
    

