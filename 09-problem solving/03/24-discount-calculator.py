amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount < 500:
    discount_pr = 0
elif amount < 1000:
    discount_pr = 5
elif amount < 2000:
    discount_pr = 10
elif amount < 5000:
    discount_pr = 15
else:
    discount_pr = 20

if amount >= 0:
    discount = amount * discount_pr / 100
    final_amount = amount - discount

    print("Original amount:", amount)
    print("Discount percentage:", discount_pr)
    print("Discount amount:", discount)
    print("Final amount:", final_amount)