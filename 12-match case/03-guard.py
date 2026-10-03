# marks = int(input("Enter the marks: "))

# match marks:
#     case i if i >= 90:
#         print("A")
#     case i if i >= 75:
#         print("B")
#     case i if i >= 60:
#         print("C")
#     case i if i >= 45:
#         print("D")
#     case _:
#         print("Fail")

day = int(input("Enter day number: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")