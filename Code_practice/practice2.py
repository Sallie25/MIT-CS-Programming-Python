cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses= 0
while abs(guess**3 -cube) >= epsilon and guess <= cube:
    print(f"\nThe current value of abs(guess**3 -cube) is {abs(guess**3 - cube)} with an epsilon of {epsilon}")
    print(f"The current guess value is {guess}")
    num_guesses+=1
    guess += increment
print('num_guesses=', num_guesses)
if abs(guess**3 -cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)