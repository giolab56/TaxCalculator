#This is a Tax Calculator

gross_income = float(input("Enter the gross income: "))

tax = 0.20

tax_deduction = 10000

dependents = int(input("Enter the number of dependents: "))

dep_deduction = dependents * 3000

income_tax = (gross_income - (dep_deduction + tax_deduction)) * tax

print(f"The income tax is ${income_tax:.1f}")
