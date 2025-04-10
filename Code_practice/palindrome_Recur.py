"""Use these examples for your checks
1. Able was I, ere I saw Elba

2. Are we not drawn onward, we few, drawn onward to new era?"""


def palindrome_Recur(x):
    def tochars(x):
        print(f'This is the value of x as requested for checks: {x}. ')
        x = x.lower()
        ans = ''
        for i in x:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                ans += i
            else:
                continue
        return ans
    
    def ispal(x):
        if len(x) <= 1:
            return True
        else:
            return x[0] == x[-1] and ispal(x[1:-1])
    return ispal(tochars(x))

pal_check = input("Enter the phrase or sentence you want to check for palindrome effect: ")
print(palindrome_Recur(pal_check))  