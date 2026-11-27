# add two numbers
# Create a lambda function that accepts two numbers and returns their sum.
add_numbers = lambda a, b: a + b
print(add_numbers(10, 20))

# find the square
# Create a lambda function that accepts one number and returns its square.
square = lambda a: a ** 2
print(square(6))

# find the cube
# Create a lambda function that accepts one number and returns the cube.
cube = lambda a: a ** 3
print(cube(3))

# check even or odd
# Create a lambda function that accepts a number and returns "Even" if the number is even, otherwise returns "Odd".
isevenodd = lambda a: "Even" if a%2 == 0 else "Odd"
print(isevenodd(7))

# find the greater number
# Create a lambda function that accepts two numbers and returns the greater number.
greater = lambda a, b: a if a>b else b
print(greater(45, 32))

# convert celsius to fahrenheit
# Create a lambda function that accepts a temperature in Celsius and converts it to Fahrenheit.
fahrenheit = lambda a: (a * 9/5) + 32
print(fahrenheit(25))

# calculate teh length of a string
# Create a lamba function that accepts a string and returns the number of characters in it.
length = lambda a: len(a)
print(length("Python"))

# convert string to uppercase
# Create a lambda function that accepts a string and returns the string in uppercase.
uppercase = lambda a: a.upper()
print(uppercase("hello world"))

# find the last character
# Create a lambda function that accepts a non-empty string and returns its last character.
last_ch = lambda a: a[-1]
print(last_ch("Coding"))

# calculate the final price
# Create a lambda function that accepts the original price and discount percentage, Return the final price after applying the discount.
final_price = lambda a, b: a - (a * b /100)
print(final_price(1000, 10))