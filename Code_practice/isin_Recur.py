"""We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be"""

# print('c' > 'a' )
# print('z' < 'c' )
# aStr_list = list(sorted_aStr)
# aStr_list.pop(middle)
# joined_str = "".join(aStr_list)
# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
    
#     returns: True if char is in aStr; False otherwise
#     '''
#     aStr = aStr.lower()
#     # sorted_aStr = "".join(sorted(aStr))
#     # print(f"Sorted string is: {sorted_aStr}")
#     high = len(aStr) - 1
#     low = 0
#     middle = ((low + high)//2)

#     if aStr == "":
#         return False

#     elif aStr[middle] == char:
#         return True
    
    
#     #"""If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)"""
#     else:
#         if aStr[middle] > char:
#             high = middle
#             aStr = aStr[0:middle]
#         else:
#             low = middle
#             aStr = aStr[middle + 1:]
        
#         return isIn(char, aStr)    

# print(isIn("H","Hello world"))


""""______________REQUIRED COD FOR SAND BOX___________________________"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    aStr = aStr.lower()
    # sorted_aStr = "".join(sorted(aStr))
    # print(f"Sorted string is: {sorted_aStr}")
    high = len(aStr) - 1
    low = 0
    middle = ((low + high)//2)

    if aStr == "":
        return False

    elif aStr[middle] == char:
        return True
    
    
    #"""If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)"""
    else:
        if aStr[middle] > char:
            high = middle
            aStr = aStr[0:middle]
        else:
            low = middle
            aStr = aStr[middle + 1:]
        
        return isIn(char, aStr)   
    

"""________________MIT'S VERSION____________________________"""
def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])


