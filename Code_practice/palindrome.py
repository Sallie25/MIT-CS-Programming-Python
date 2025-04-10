"""phrases and sentences to check my code:- 

"madam" ✅
"racecar" ✅
"civic" ✅
"Was it a car or a cat I saw" ✅
"A man, a plan, a canal, Panama!" ✅
"No lemon, no melon" ✅
"Step on no pets." ✅
"Never odd or even" ✅
"Eva, can I see bees in a cave?" ✅
"Mr. Owl ate my metal worm." ✅

"Hello, world!" ❌
"Python is fun" ❌
"Palindrome check" ❌
"I love coding" ❌
"ChatGPT is amazing" ❌
"Dogs and cats" ❌
"This is not a palindrome" ❌
"AI will change the world" ❌
"OpenAI is smart" ❌
"I am not a palindrome"

"raceecar" ❌ (Extra 'e' in the middle)
"Was it a rat or a cat I saw" ❌ (Wrong word: 'rat' instead of 'car')
"A man, a plan, a canal, Panam!" ❌ (Missing 'a' at the end)
"Never even or odd" ❌ (Rearranged 'even' and 'odd')
"Step on no petz." ❌ (Ends with 'z' instead of 's')
"Mr. Owl ate my metal worn." ❌ ('worm' changed to 'worn')
"Eva, can I see bees in a cake?" ❌ ('cave' changed to 'cake')
"Do geese see Dog?" ❌ ('God' changed to 'Dog')
"No lemon, one melon" ❌ ('no' changed to 'one')
"Madam, in Ede, I'm Adam" ❌ ('Eden' shortened to 'Ede')

"""

# def palindrome_Iter(x):
#     def tochar(x):
#         x = x.lower()
#         ans = ''
#         for _ in x:
#             if _ in "abcdefghijklmnopqrstuvwxyz":
#                 ans += _
#             else:
#                 continue  
#         return ans
#     def ispal_iter(x):
#         if len(x) <= 1:
#             return True
#         else:
#             first = 0
#             last = -1
#             list_truity = []
#             for i in range(len(x)):
#                 if x[first] == x[last]:
#                     first += 1
#                     last -= 1
#                     p = True
#                     list_truity.append(p)
#                 else:
#                     return False    
                
#             summation = True
#             for j in list_truity:
#                 return j == summation
#     return ispal_iter(tochar(x))
# pal_check = input("Enter the phrase or sentence you want to check for palindrome effect: ")
# print(palindrome_Iter(pal_check))  

def palindrome_Iter(x):
    def tochar(x):
        x = x.lower()
        ans = ''
        for _ in x:
            if _ in "abcdefghijklmnopqrstuvwxyz":
                ans += _
            else:
                continue  
        return ans
    def ispal_iter(x):
        if len(x) <= 1:
            return True
        else:
            first = 0
            last = -1
            list_truity = []
            for i in range(len(x)):
                if x[first] != x[last]:
                    return False
                else:
                    first += 1
                    last -= 1    
                
    return ispal_iter(tochar(x))
pal_check = input("Enter the phrase or sentence you want to check for palindrome effect: ")
print(palindrome_Iter(pal_check))  

