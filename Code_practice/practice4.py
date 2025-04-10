num = int(input('Enter desired value:- '))
if num < 0:
   isNeg= True
   num = abs(num)
else:
   isNeg= False
result = ''
if num == 0:
   result = "0"
while num > 0:
   result = str(num%2) + result
   print(f"\n Current value of str(num%2) is {str(num%2)} and result is {result}")
   num = num//2
   print(f"Its corresponding num value is {num}")
if isNeg:
   result = "-" + result
print(result)   