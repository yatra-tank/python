balance = 30000

def check_balance(balance):
    print("Current Balance:", balance)

def credit_balance(balance, amt):
    balance += amt
    print("Amount credited successfully!")
    return balance

def withdrawal(balance, amt):
    if amt <= balance:
        balance -= amt
        print("Amount withdrawn successfully!")
    else:
        print("Insufficient balance!")
    return balance


while True:
    print("""
---OPERATIONS---
1. CHECK BALANCE
2. CREDIT BALANCE
3. WITHDRAWAL
4. EXIT
""")

    n = input("Enter your choice: ")

    if n == "1":
        check_balance(balance)

    elif n == "2":
        amt = int(input("Enter amount to credit: "))
        balance = credit_balance(balance, amt)

    elif n == "3":
        amt = int(input("Enter amount to withdraw: "))
        balance = withdrawal(balance, amt)

    elif n == "4":
        print("Exited")
        break

    else:
        print("Invalid choice!")