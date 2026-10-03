# Create a simple mobile settings menu:
# 1 → Wi-Fi
# 2 → Bluetooth
# 3 → Mobile Data
# 4 → Airplane Mode
# 5 → Exit
# Take the user's choice and display the selected setting.

print("""--- MOBILE SETTINGS MENU ---
1. Wi-Fi
2. BLUETOOTH
3. MOBILE DATA
4. AIRPLANE MODE
5. EXIT""")

n = int(input("Enter your order: "))

match n:
    case 1:
        print("Wi-Fi seleced.")
    case 2:
        print("Bluetooth selected.")
    case 3:
        print("Mobile data selected.")
    case 4:
        print("Airplane mode selected.")
    case 5:
        exit()
    case _:
        print("Invalid menu choice.")