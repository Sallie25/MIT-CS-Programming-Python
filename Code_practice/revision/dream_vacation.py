"""Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
"""

flag = True
responses = {}

while True:
    username = input("Enter name: ")
    dream_vacation = input("If you could visit one place in the world,where would you go? ")
    prompt = input("Do we have any more responses yes/no?")
    if prompt == 'no':
        break
    else:
        responses[username] = dream_vacation

print("Below are the list of responses: \n") 
for name, vacation_spot in responses.items():
    print(f"{name.title()} dream vacation spot is {vacation_spot.title()}.")        

# while flag:
#     username = input("Enter name: ")
#     dream_vacation = input("If you could visit one place in the world,where would you go? ")
    
#     responses[username] = dream_vacation

#     prompt = input("Do we have any more responses yes/no?")
#     if prompt == 'no':
#         flag = False   

# print("Below are the list of responses: \n") 
# for name, vacation_spot in responses.items():
#     print(f"{name.title()} dream vacation spot is {vacation_spot.title()}.")