name = "Yatra"
city = "Kalol"
course = "Python"
age = 17

print(name)
print(city)
print(course)
print(age)

text = "Python Programming"

print(text)
print(len(text))
print(text[0])
print(text[2])
print(text[-1])
print(text[-2])

text = "Programming"

print(text[0])
print(text[1])
print(text[4])
print(text[-1])
print(text[-2])
print(text[-3])
print(text[-len(text)])

text = "Python Programming"

print(text[:6])
print(text[7:])
print(text[:])
print(text[:5])
print(text[-5:])

text = "ABCDEFGHIJKL"

print(text[::2])
print(text[::3])
print(text[1:9:2])
print(text[::-1])

text = input("Enter a string: ")

print(len(text))
print(text[0])
print(text[-1])

a = "Python"
b = "python"

print(a == b)
print(a.lower() == b.lower())

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = first_name + " " + last_name

print(full_name)

name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")
language = input("Enter programming language: ")

print("My name is " + name + ", I am " + str(age) + " years old, I live in " + city + " and I am learning " + language + ".")

symbol = "*"

print(symbol * 3)
print(symbol * 5)
print(symbol * 10)

text = "python programming language"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

text = "Python is a programming language"

print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)

print(text.find("Python"))
print(text.find("programming"))
print(text.find("language"))
print(text.find("Java"))

text = "banana"

print(text.count("a"))
print(text.count("n"))
print(text.count("b"))

filename = "student_notes.pdf"

print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))

text = "I am learning Java"

print(text.replace("Java", "Python"))

text = "apple apple apple"

print(text.replace("apple", "mango"))
print(text.replace("apple", "mango", 1))

text = "Python"

text.upper()
print(text)

text = text.upper()
print(text)

text = "   Python Programming   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

name = input("Enter your name: ")

name = name.strip()

print(name)

text = "Python is easy to learn"

print(text.split())

text = "apple,banana,mango,orange"

print(text.split(","))

words = ["Python", "is", "easy"]

print(" ".join(words))
print("-".join(words))
print("/".join(words))

name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")

print(f"My name is {name}, I am {age} years old and I live in {city}.")

a = 10
b = 20

print(f"The sum is {a + b}")

name = input("Enter your full name: ")

cleaned = name.strip()

print(name)
print(cleaned)
print(cleaned.upper())
print(cleaned.lower())
print(cleaned.title())
print(len(cleaned))
print(cleaned[0])
print(cleaned[-1])
print("a" in cleaned.lower())

sentence = input("Enter a sentence: ")

print(sentence)
print(len(sentence))
print(len(sentence.split()))
print(sentence[0])
print(sentence[-1])
print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print("Python" in sentence)
print(sentence.lower().count("a"))

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = input("Enter age: ").strip()

full_name = first_name + " " + last_name

print(full_name.title())
print(full_name.upper())
print(full_name.lower())
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(city)
print(course)
print(f"Age: {age}")
print("Python" in course)
print(course.replace("Python", "Java"))
print(len(course.split()))

text = input("Enter a string: ")

print(text[:3])
print(text[-3:])
print(text[::2])
print(text[::-1])
print(text[1:-1])