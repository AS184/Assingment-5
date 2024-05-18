print("Enter your last name")
lname = input()
print("Enter number of dependents ")
dependents = int(input())
print("Enter gross income ")
gross = float(input())
adjgross = gross - dependents * 12000
if adjgross > 50000:
  taxrate = adjgross * 0.2
else:
  taxrate = adjgross * 0.1

tax = taxrate * gross

if tax < 0:
  tax = 100

print("Last name: ", lname)
print("Gross income: $", gross)
print("Number of dependents: ", dependents)
print("Adjusted gross income: $", adjgross)
print("Income tax: $", tax)