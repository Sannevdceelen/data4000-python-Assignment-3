#Bank loan repayment simulator
#skills: while loops, math, functions

def monthly_interest_rate(annual_rate_percent):
    return annual_rate_percent / 100 / 12

loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
monthly_payment = float(input("Enter the monthly payment amount: "))

rate = monthly_interest_rate(annual_interest_rate)

balance = loan_amount
month = 0

if monthly_payment <= balance * rate:
    print("\nThe monthly payment is too low to cover the interest. The loan will never be repaid.")
else:
    while balance > 0:
        balance = balance + (balance * rate)
        if monthly_payment > balance:
            monthly_payment_this_month = balance
        else:
            monthly_payment_this_month = monthly_payment
        
        balance -= monthly_payment_this_month
        month += 1

    print(f"\nIt will take {month} months to repay the loan.")
    