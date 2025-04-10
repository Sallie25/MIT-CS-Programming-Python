"""Implementing the Fibonnaci mathematical Principle to code
where n = number of months, so the number of females in n month is,
females(n) = females(n-1) + females(n-2).

Also, we get see cases where recursion works with two base cases.
"""
# def fib(x):
#     """Assume x  as an int>=0 returns fibonnacci of x"""
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)
# print(fib(7))   
# 
#  
def fibIter(x):
    females = 0
    all_females = []
    for i in range(x+1):
        if i == 0 or i == 1:
            females = 1
            all_females.append(females)
            print(f'current value of {i} is {females}') 
        else:
          females = females + all_females[-2]
          print(f'current value of {i} is {females}') 
          all_females.append(females)
             
    return females
print(fibIter(7))
        