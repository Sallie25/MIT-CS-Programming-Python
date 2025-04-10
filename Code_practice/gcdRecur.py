"""_____MIT's ANSWER_____"""
# def gcdRecur(a, b):
#     '''
#     a, b: positive integers
    
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Base case is when b = 0
#     if b == 0:
#         return a

#     # Recursive case
    # return gcdRecur(b, a % b)   
    
""""_____MY ANSWER_____"""
def gcdRecur(a, b):
    if a >= b and a % b == 0:
        return b
    elif b >= a and b % a == 0:
       return a
    else:
        return gcdRecur(b, a % b) 
print(gcdRecur(255, 255))        