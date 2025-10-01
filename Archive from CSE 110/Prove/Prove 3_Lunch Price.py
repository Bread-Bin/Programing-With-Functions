print("Welcome to the BYU-I Cafateria")

print("Please enter in the proper information below")
print("__" * 12)
print(" ")
meal_c = float(input("Child Meal Price: $"))
meal_a = float(input("Adult Meal Price: $"))
drinks = float(input("Drink Price: $"))
num_c = int(input("Number of Children: "))
num_a = int(input("Number of Adults: "))
num_d = int(input("Number of Drinks: "))
tax = float(input("Sale Tax Rate: "))

meal_price_c = meal_c * num_c
meal_price_a = meal_a * num_a
drink_price = drinks * num_d

print(" ")

price_total = meal_price_c + meal_price_a + drink_price
print(f"Subtotal: ${price_total:.2f}")

tax_total = price_total * tax / 100
print(f"Sale Tax: ${tax_total:.2f}")

sale_total = price_total + tax_total
print(f"Total: ${sale_total:.2f}")

print("")

payment = float(input("What is the payment amount?: $"))
change = payment - sale_total
print(f"Change: ${change:.2f}")

print(" ")
print("Have a Nice Day")