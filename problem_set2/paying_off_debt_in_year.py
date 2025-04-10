"""Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy

A summary of the required math is found below:

Monthly_interest_rate= (Annual interest rate) / 12.0
Minimum_monthly_payment = (Minimum monthly payment rate) x (Previous balance)
Monthly_unpaid_balance = (Previous balance) - (Minimum monthly payment)
Updated_balance_each_month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
Monthly_interest_rate = (annualInterestRate) / 12.0

for _ in range(1,13):
            Minimum_monthly_payment = monthlyPaymentRate * balance
            Monthly_unpaid_balance = balance - Minimum_monthly_payment
            Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance) 
            balance = Updated_balance_each_month
            print("Month ", _ , "Remaining balance: ", round(balance,2))
            
print("Remaining balance:", round(balance,2))            