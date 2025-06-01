original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

discount_amount = (discount_percent / 100) * original_price
final_price = original_price - discount_amount

print("Discount amount is:", discount_amount)
print("Final price after discount is:", final_price)
