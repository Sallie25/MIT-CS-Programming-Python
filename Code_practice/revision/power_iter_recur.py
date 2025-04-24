"""Returns base raise to the power exp. where base can either be an int or float. 
However exp must be an int. Also we cannot use '**'. Should return a single value"""
# def iter_power(base, exp):
#     power = 0
#     value = base
#     for i in range(exp-1):
#         power = value * base
#         value = power
#     return power
# print(iter_power(2, 5))

def iter_recur(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * iter_recur(base, exp - 1)
print(iter_recur(3, 4))    