print("""--- OPERATIONS---
1. BILLING
2. TECHNICAL SUPPORT
3. ORDER TRACKING""")

n = int(input("Enter your desired operation: "))

match n:
    case 1:
        print("""--- BILLING ---
        1. REQUEST REFUND
        2. DISPUTE A CHARGE""")

        a = int(input("Enter desired issue:"))

        match a:
            case 1:
                print("Your refund request has been registered.")
            case 2:
                print("Dispute for a charge is on review.")
            case _:
                print("Invalid billing operation.")

    case 2:
        print("""--- TECHINICAL SUPPORT ---
        1.PASSWORD RESET
        2.APP CRASHING""")

        a = int(input("Enter desired issue:"))
        
        match a:
            case 1:
                print("Your password has been reset.")
            case 2:
                print("The app will be recovered soon.")
            case _:
                print("Invalid operation.")

    case 3:
        print("""--- ORDER TRACKING ---
         1. VIEW DELIVERY ADDRESS
         2. CHANGE SHIPPING ADDRESS""")

        a = int(input("Enter desired issue:"))
        
        match a:
            case 1:
                print("Delivery Address as follows: .")
            case 2:
                print("Shipping address is successfully changed.")
            case _:
                print("Invalid operation.")

    case _:
        print("Invalid option.")