"""Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""
print("----Types of sandwiches Available----\n")
sandwich_orders = ["Turkey & Cheese", "Pastrami on Rye", "Chicken Club", "Veggie Delight", "Tuna Melt",  
                   "BLT", "Ham & Swiss", "Pastrami on Rye", "Philly Cheesesteak", "Grilled Cheese",  
                   "Buffalo Chicken", "Egg Salad", "Roast Beef & Cheddar", "Pastrami on Rye", "Italian Sub"]

finished_sandwiches = []
print(sandwich_orders)
print()
while "Pastrami on Rye" in sandwich_orders:
    sandwich_orders.remove("Pastrami on Rye")
print("----Deli has run out of pastrami!!!!-----\n")    
print(f"Available sandwiches are:- {sandwich_orders}")    
