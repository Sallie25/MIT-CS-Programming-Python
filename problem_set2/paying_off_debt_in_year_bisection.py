# original_balance = 999999
# annualInterestRate = 0.18
# Monthly_interest_rate = (annualInterestRate) / 12.0
# monthly_payment_lower_bound = original_balance/12
# monthly_payment_upper_bound = (original_balance * pow((1 + Monthly_interest_rate), 12) / 12.0)


# while True: 
#         balance = original_balance  
#         Minimum_fixed_monthly_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2      
#         for _ in range(1,13):
#             Monthly_unpaid_balance = balance - Minimum_fixed_monthly_payment
#             Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance) 
#             balance = Updated_balance_each_month
#             print("Month ", _ , "Remaining balance: ", round(balance,2))
#             print("\nThe lowest payment:","for month",_ ,Minimum_fixed_monthly_payment)
            
#         if balance > 0:
#             monthly_payment_lower_bound = Minimum_fixed_monthly_payment
#         elif balance < 0:
#              monthly_payment_upper_bound = Minimum_fixed_monthly_payment    
#         else:
#             print("\nThe lowest payment:",Minimum_fixed_monthly_payment)
#             break    


# original_balance = 320000
# annualInterestRate = 0.2
# Monthly_interest_rate = (annualInterestRate) / 12.0
# monthly_payment_lower_bound = original_balance/12
# monthly_payment_upper_bound = (original_balance * ((1 + Monthly_interest_rate)**12) / 12.0)



# while True: 
#         balance = original_balance  
#         Minimum_fixed_monthly_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2      
#         for _ in range(1,13):
#             Monthly_unpaid_balance = balance - Minimum_fixed_monthly_payment
#             Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance) 
#             balance = Updated_balance_each_month
#             print("Month ", _ , "Remaining balance: ", round(balance,2))
#             print("\nThe lowest payment:","for month",_ ,Minimum_fixed_monthly_payment)


#         if abs(monthly_payment_upper_bound - monthly_payment_lower_bound) < 0.01:
#              print("\nThe lowest payment:", round(Minimum_fixed_monthly_payment, 2))
#              break    
#         elif balance > 0:
#             monthly_payment_lower_bound = Minimum_fixed_monthly_payment
#         elif balance < 0:
#              monthly_payment_upper_bound = Minimum_fixed_monthly_payment    
        

# Define initial parameters
original_balance = 320000  # Principal amount
annualInterestRate = 0.2  # Annual interest rate

# Calculate monthly interest rate
Monthly_interest_rate = annualInterestRate / 12.0

# Define search boundaries
monthly_payment_lower_bound = original_balance / 12  # Paying off with no interest
monthly_payment_upper_bound = (original_balance * (1 + Monthly_interest_rate) ** 12) / 12  # Paying off with compounded interest

# Bisection search loop
while True:
    balance = original_balance  # Reset balance for each iteration
    Minimum_fixed_monthly_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2  # Midpoint
    
    # Simulate a year of payments
    for _ in range(12):
        Monthly_unpaid_balance = balance - Minimum_fixed_monthly_payment
        Updated_balance_each_month = Monthly_unpaid_balance + (Monthly_interest_rate * Monthly_unpaid_balance)
        balance = Updated_balance_each_month
    
    # Check if balance is close enough to zero
    if abs(balance) < 0.01:
        print("\nThe lowest payment:", round(Minimum_fixed_monthly_payment, 2))
        break  # Exit loop when an accurate estimate is found
    
    # Adjust search bounds
    elif balance > 0:
        monthly_payment_lower_bound = Minimum_fixed_monthly_payment  # Increase lower bound if balance is still positive
    else:
        monthly_payment_upper_bound = Minimum_fixed_monthly_payment  # Decrease upper bound if balance goes negative
    

