# A shop gives discounts based on purchase amount. If the purchase amount is greater than or equal to 1000, a discount of 10% is given. If the purchase amount is between 500 and 999, a discount of 5% is given. If the purchase amount is less than 500, no discount is given. Calculate and print the final amount to be paid after applying the discount.
purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount >= 1000:
    discount = purchase_amount * 0.10
elif 500 <= purchase_amount < 1000:
    discount = purchase_amount * 0.05
else:
    discount = 0
final_amount = purchase_amount - discount
print("Final amount to be paid after discount:", final_amount)