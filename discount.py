def  calculate_discount(price, discount_percent):
    discounted_price=price-(price*discount_percent/100)
    return discounted_price
price=float(input("Enter the price of the item"))
discount_percent=float(input("Enter the discount"))
if discount_percent >=20:
    result = calculate_discount(price, discount_percent)
    print("You will pay",result)
else:
    print("Yuo will pay",price)
       
