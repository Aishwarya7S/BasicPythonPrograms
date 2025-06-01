principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest is:", compound_interest)
