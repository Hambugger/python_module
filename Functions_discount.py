def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discount_amount = price * (discount_percent /100)
    final_price = price - discount_amount
  else:
    final_price = price
  return final_price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the prce of the discount percent: "))
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount is: $",final_price)
    