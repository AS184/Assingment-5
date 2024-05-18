print("Enter appliance name")
appliance_name = input()

print("Enter appliance price")
appliance_price = int(input())
warranty_cost = 0

if appliance_price <= 1000:
    warranty_cost = appliance_price * 0.10
  else
  appliance_price * 0.05

print("Appliance name: ", appliance name)
print("Appliance price: ", appliance_price)
print("Warranty cost: ", warranty_cost)
print("Total cost: ", appliance_price + warranty_cost)