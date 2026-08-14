# write a function called discount_price that takes original_price and discount_percent as parameters and print final price after discount

def discount_price(original_price, discount_percent):
    discount_pr = original_price * discount_percent / 100
    final_price = original_price - discount_pr
    print('WOW You get discount of Rs.',discount_pr,"& final amount you have to pay is", final_price)
discount_price(100, 20)