# A restaurant has the following menu:
# 1 → Pizza
# 2 → Burger
# 3 → Pasta
# 4 → Sandwich
# Write a program that takes the customer's choice and displays the selected food.
print("""--- RESTUARANT MENU ---
1. PIZZA
2. BURGER
3. PASTA
4. SANDWICH""")

n = int(input("Enter your order: "))

match n:
    case 1:
        print("You've selected pizza.")
    case 2:
        print("You've selected burger.")
    case 3:
        print("You've selected pasta.")
    case 4:
        print("You've selected sandwich.")
    case _:
        print("Invalid setting.")