total = 0
budget = 0
regular = 0
premium = 0
luxury = 0

for i in range(8):
    n = float(input("Enter price: "))
    total += n

    if n < 500:
        budget += 1
        print("Budget")
    elif n < 2000:
        regular += 1
        print("Regular")
    elif n < 5000:
        premium += 1
        print("Premium")
    else:
        luxury += 1
        print("Luxury")

print("Total:", total)
print("Budget:", budget)
print("Regular:", regular)
print("Premium:", premium)
print("Luxury:", luxury)
print("Average:", total / 8)