# message = "global"

# def lvl1():
#     # global message
#     message = "enclosing"
#     L =[1, 2, 3, 4, 5]

#     def lvl2():
#         nonlocal message
#         message = "added"
#         print(L)

#         def lvl3():
#             nonlocal message
#             message = "level 3"
#         lvl3()

#     lvl2()
#     # print(message)

# lvl1()

# # print(message)

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
print(counter())