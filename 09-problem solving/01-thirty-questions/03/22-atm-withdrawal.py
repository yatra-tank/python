balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= 0:
    print("Invalid withdrawal amount")
elif withdraw % 100 != 0:
    print("Withdrawal amount must be divisible by 100")
elif withdraw > balance:
    print("Insufficient balance")
elif balance - withdraw < 500:
    print("At least ₹500 must remain")
else:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)