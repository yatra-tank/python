# # Write a program that keeps asking the user for numbers.
# while True:
#     n = int(input("Enter a number, enter zero to stop: "))
#     if n > 0:
#         print(n)
#     elif n < 0:
#         continue
#     else:
#         break

# numbers = [12, 5, -4, 18, 0, 25, 30]
# for i in numbers:
#     if i < 0:
#         continue
#     elif i == 0:
#         break
#     else:
#         print(i)

# # Write a program that searches for a number in a list.
# L = eval(input("Enter a list of numbers: "))
# n = int(input("Enter the required number: "))
# for i in L:
#     if i == n:
#         print("Number found")
#         break
# else:
#     print("Number not found")