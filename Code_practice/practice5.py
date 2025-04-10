x = float(input('Enter a decimal number between 0 and 1: '))
p = 0
while ((2**p) * x) % 1 != 0:
    """MY FUTURE SELF - If this part of the code confuses you remember chatgpt(sallieakpan@gmail.com - code termination analysis sub heading).This line of code helps us extract the fraction part of the result from the whole number. Hence, int((2**p) * x) this gives us an integer value of the decimal whilst (2**p) * x without the int returns the float version of tHE COMPUTATION.
    
    The end goal is to increase p - the power enough that this computation (2**p) * x - int((2**p) * x) eventually amounts to 0. Then you can sy that you have gotten the whole the power value that is raised by 2 and multiplied to the deciml number you want to find the binary of that then amounts to a whoe number.
     
     """
    print('Remainder= ' + str((2**p) * x - int((2**p) * x)))
    p += 1

num = int(x * (2**p)) # The p value that gives that doesnt leave a remainder is used here to obtain the whole number
result = ''

if num == 0: 
    result = '0'

while num > 0:# We use the whole number hear to obtain its binary the old fashion way as seen in practice 4
    result = str(num % 2) + result # Divide and output the remainder
    num = num // 2 # divide and round down

for i in range(p - len(result)): # for i in range(3 - 2), remainder thar result is a string hence the use of the function len.
    print(f"current value of i is {i}")
    result = '0' + result # since p = 3 we are expecting three digits after the decimal point not 2.
    print(f"current value of result is {result}")
"""
result[0:-3] → Everything before the last 3 digits → "" (empty)
result[-3:] → The last 3 digits → "101" or "011"
"""
result = "0" + result[0:-p] + '.' + result[-p:]

print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
