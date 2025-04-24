"""The greatest common divisor is the largest integer that divides two values without remainder. Examples:-
(17, 12),1
(2, 12),2
(9, 12),3"""

# def gcditer(a, b):
#     list_of_factors = []

#     def minimum(a, b):
#         if a < b:
#             return a
#         return b
    
#     def maximum(value_list):
#         return value_list[-1]
    
#     if a % minimum(a, b) == 0 and b % minimum(a, b) == 0:
#         return minimum(a, b)
    
#     else:
#         for i in range(1, minimum(a, b) + 1):
#             if a % i == 0 and b % i == 0:
#                 list_of_factors += [i]
          
#     return maximum(list_of_factors)

# print(gcditer(12, 17))

def gcdrecur(a, b):

    if a >= b and a % b == 0:
        return b
    elif b >= a and b % a == 0:
        return a
    # if b == 0:
    #     return a
    else:
        return gcdrecur(b, a % b)
print(gcdrecur(17, 12))    