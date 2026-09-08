answer = input("Do you have an ID? ").lower().strip()

if answer == "yes":
    answer = True
elif answer == "no":
    answer = False
else:
    print("invalid input")
    answer = None

if answer:
    print("welcome")
elif answer:
    print("bring ID")