units = float(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity bill =", bill)
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
    print("Electricity bill =", bill)
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("Electricity bill =", bill)