"""A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: (0.25*n*s**2)/tan(π/n)

The perimeter of a polygon is: length of the boundary of the polygon
This means that:-
P is the summation of the sides length(s) from i= 1 to n

However,
For a regular polygon (where all sides are equal), the formula simplifies to:
P= n * s
where:
n is the number of sides
s is the length of each side

Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
"""
#import the math module
import math
# def a polysum function that takes in two arguments
def polysum(n, s):

    '''input values for s and n
    return rounded sum of the area and 
    squared perimeter rounded to 4 decimal places'''
    
    
    # find the area of the polygon,calling the math module on tan and pi
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    
    #find the perimeter of a polygon with equal sides s
    perimeter = n * s
    
    #return the sum of the area and squared perimeter rounded to 4 decimal places
    return round((area + perimeter**2), 4)

