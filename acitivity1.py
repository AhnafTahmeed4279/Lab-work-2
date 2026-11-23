print("E-Commerce Free delivery eligibility")
weight=float(input("Enter the cart weight in kg: "))
cart_value=int(input("Enter the cart value in taka:"))
if weight<5 or cart_value>=1500:
    print("Delivery Status:FREE SHIPPING")
else:
    print("Delivery Status:Shipping charges apply")
    