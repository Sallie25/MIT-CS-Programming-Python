"""Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc"""

# s = 'azcbobobegghakl'
# print(f"Raw form: {s[0:2]}")
# print(f"Sorted format: {''.join(sorted(s[0:2]))}")
# print(f"Comparison: {s[0:2] == ''.join(sorted(s[0:2]))}")

# s = 'fxgomncqnwctzvzd'
#s = 'azcbobobegghakl'
s = "tgxrheyfplivcqsrlaemjmec"
sorted_string = []
start = 0
end = 1
required_string = []
for i in range(len(s)):
    # sorted outputs a list so we need .join to change it to a string to enable truity in comparison.
    if s[start:end] == ''.join(sorted(s[start:end])): 
        #if the above is true, it adds the string to the list called sorted_string
        sorted_string.append(s[start:end])
        #Increase the only the end value by one
        end += 1
    #If the above condition is false, increase the start value and end value by one    
    else:
        start += 1
        end += 1 

#From the list "sorted string", find the string value in it with the longest character length and house it in the container "longest word" with the hep of the function max and the parameter "key"      
longest_word = max(sorted_string, key=len)
print("Longest substring in alphabetical order is: " + longest_word)        

# print(start)
# print(end)
# print(sorted_string)

# for j in sorted_string:
#     if j == ''.join(sorted(j[:])):
#         required_string.append(j)
# longest_word = max(required_string, key=len)
# print("Longest substring in alphabetical order is: " + longest_word)

