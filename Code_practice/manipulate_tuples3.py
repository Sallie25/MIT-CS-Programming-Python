x = (1, 2, (3, 'John', 4), 'Hi')

tup1 = (5)
print(f"The value of tupl1 is {tup1} and its data type is {type(tup1)} ")

tup2 =(5,) 
print(f"The value of tupl2 is {tup2} and its data type is {type(tup2)} ")

"""______EXERCISE_1______"""
print(f"The value of x[0] is {x[0]}\n")
print(f"The value of x[2] is {x[2]}\n")
print(f"The value of x[-1] is {x[-1]}\n")
print(f"The value of x[2][2] is {x[2][2]}\n")
print(f"The value of x[2][-1] is {x[2][-1]}\n")
print(f"The value of x[-1][-1] is {x[-1][-1]}\n")
# print(f"The value of x[-1][2] is {x[-1][2]}\n")
print(f"The value of x[0:1] is {x[0:1]}\n")
print(f"The value of x[0:-1] is {x[0:-1]}\n")
print(f"The value of len(x) is {len(x)}\n")
print(f"The value of 2 in x is {2 in x}\n")
print(f"The value of 3 in x is {3 in x}\n")
print(f"The value of 3 in x[2] is {3 in x[2]}\n")

# x[0] = 8 # Tuple object does not support item assignment.
