import math, time

print("Shopping Helper 005!")

#lists
cart = []
price = []

while True:
    #Commands
    time.sleep(2)
    print('''\nPlease select one of the following options:\n
    1. Add Item
    2. View Cart
    3. Remove Item
    4. Compute total
    5. Finish''')

    choice = input("\nEnter your choice (1-5): ")

    #Enter in Item & Price
    if choice == "1":
        item = input("Enter the item name: ").capitalize()
        cart.append(item)

        #price verificcation fix
        valid_price = False
        while not valid_price:
            try:
                item_price = float(input("Enter the price of the item: $"))
                valid_price = True
            except ValueError:
                print("Invalid price. Please enter in a vaild number.")
        
        price.append(item_price)
        print(f"{item} has been added to the cart.")
    
    #View Cart
    elif choice == "2":
        print("\nCart:")
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("Item                            Price")
            print("-------------------------------------")            
            for i in range(len(cart)):
                print(f"{i + 1:2}. {cart[i]:<25}  ${price[i]:.2f}")
        time.sleep(2)

    #Remove Items
    elif choice == "3":

        if len(cart) == 0:
            print("Your cart is empty.")
        
        else:
            print("\nCart:")
            print("Item                            Price")
            print("-------------------------------------")            
            #print cart with numbers
            for i in range(len(cart)):
                item = cart[i]
                print(f"{i + 1:2}. {item:<25}  ${price[i]:.2f}")
            item_index = int(input("\nEnter the number of the item you wish to remove: "))

            if item_index < 1 or item_index > len(cart):
                print("Invalid Item Number.")
            else:
                removed_item = cart.pop(item_index - 1)
                removed_price = price.pop(item_index - 1)
                print(f"Removed {removed_item} from cart.")
        
    #Final Total
    elif choice == "4":

        if len(cart) == 0:
            print("Your cart is empty.")
        
        else:
            print("\nCompute Total:")
            time.sleep(1)
            print("Calculating Total...")
            time.sleep(4)
            total = sum(price)
            sales_tax = total * 0.08

            print("\nTotal Item Count: {}".format(len(cart)))
            print("-" * 25)
            print("{:<12} {}".format("Subtotal:", "${:.2f}".format(total)))
            print("{:<12} {}".format("Sales Tax:", "${:.2f}".format(sales_tax)))
            print("-" * 25)
            print("{:<12} {}".format("Final Total Price:", "${:.2f}".format(total + sales_tax)))
            time.sleep(2)
    
    #Finish
    elif choice == "5":

        if len(cart) == 0:
            print("Your cart is empty.")

        else:
            print("\nFinal Cart:")
            print("Item                            Price")
            print("-------------------------------------")
            for i in range(len(cart)):
                print(f"{i + 1:2}. {cart[i]:<25}  ${price[i]:.2f}")
            total = sum(price)
            sales_tax = total * 0.08

            print("\nTotal Item Count: {}".format(len(cart)))
            print("-" * 25)
            print("{:<12} {}".format("Subtotal:", "${:.2f}".format(total)))
            print("{:<12} {}".format("Sales Tax:", "${:.2f}".format(sales_tax)))
            print("-" * 25)
        print("{:<12} {}".format("Final Total Price:", "${:.2f}".format(total + sales_tax)))
        print("\nThank you for using Shopping Helper 005!")
        break

    else:
        print("Invalid Entry. Please try again using numbers 1-5.")

