'''E-commerce Coupon Application
Apply coupon only if order ≥2000 and coupon valid.'''

order=int(input("enter your order: "))

def E_commerce_Coupon_Application(order):
    if order>=2000:
        print("coupon valid")
    else:
        print("coupon NOT valid")
E_commerce_Coupon_Application(order)