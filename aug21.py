
def calculate_apple_order():
    apple_buying = int(input("Please enter the quantity of the apples you wish to purchase: "))
    if apple_buying < 10:
        price = 0.75
    else:
        price = 0.50
        
    order = apple_buying * price
    if apple_buying > 50:
        order *= 0.90  # Apply a 10% discount on the total

    print(f"Your order of {apple_buying} apples will cost ${order:.2f}.")

calculate_apple_order()

  
    
