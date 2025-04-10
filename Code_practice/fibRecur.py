def fibRecur(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fibRecur(x-1) + fibRecur(x-2)
print(fibRecur(7))    