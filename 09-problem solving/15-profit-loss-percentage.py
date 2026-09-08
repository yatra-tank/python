cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if cp <= 0:
    print("Invalid cost price")
elif sp > cp:
    profit = sp - cp
    percentage = profit / cp * 100
    print("Profit =", profit)
    print("Profit percentage =", percentage)
elif sp < cp:
    loss = cp - sp
    percentage = loss / cp * 100
    print("Loss =", loss)
    print("Loss percentage =", percentage)
else:
    print("No profit and no loss")