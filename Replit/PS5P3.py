print("Quantity of books")
book_quantity = int(input())
print("Price per book")
book_price = int(input())
total_price = book_quantity * book_price
shipping_cost = 0
if total_price <= 50:
    shipping_cost = 25
  else
shipping_cost = 0

print("Total price: ", total_price),
print("Shipping cost: ", shipping_cost)
