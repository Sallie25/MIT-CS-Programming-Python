epsilon = 0.01
y= float(input("Enter desired values: "))
guess = y/2.0
numGuesses= 0
while abs(guess*guess -y) >= epsilon:
    numGuesses+= 1
    guess = guess -(((guess**2) -y)/(2*guess))
print('numGuesses= ' +str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))