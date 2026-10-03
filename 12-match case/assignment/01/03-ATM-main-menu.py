# Create an ATM menu:
# 1 → Check Balance
# 2 → Withdraw Money
# 3 → Deposit Money
# 4 → Change PIN
# 5 → Exit
# Take the user's choice and display the corresponding message.

print("""--- ATM MENU ---
1. CHECK BALANCE
2. WITHDRAW MONEY
3. DEPOSIT MONEY
4. CHANGE PIN
5. EXIT""")

n = int(input("Enter your order: "))

match n:
    case 1:
        print("Check balance seleced.")
    case 2:
        print("Withdraw money selected.")
    case 3:
        print("Deposit money selected.")
    case 4:
        print("Change pin selected.")
    case 5:
        exit()
    case _:
        print("Invalid menu choice.")