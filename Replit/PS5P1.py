print("Enter quantity of item")
quantity = int(input())
unit_price = 100
if quantity >= 1000:
    unit_price = 3
else:
    unit_price = 5

extended_price = quantity * unit_price

tax_rate = 0.07

tax = extended_price * tax_rate

total = extended_price + tax

print("Quantity:", quantity),
print("Unit price:", unit_price),
print("Extended price:", extended_price),
print("Tax:", tax),
print("Total:", total)