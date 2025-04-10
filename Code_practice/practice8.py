def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_b')
    return y
def func_c(z):
    print('inside func_c')
    return z() # So, the reason why we have the parantheses after z is because the argument for the parameter z is a function
func_a()
print(5 + func_b(2))
print(func_c(func_a))