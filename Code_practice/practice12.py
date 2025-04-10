def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
x = int(input('Enter value: '))
print(factorial(x))  