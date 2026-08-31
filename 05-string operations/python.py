# word = "Python"
# print(word[:3].upper() + word[3:].lower() )

# a = " pYTHON"
# print(a.capitalize())

# a = """pYTHON ∴ ⊍ 🀃	𞲖	𞲠𞲡	𞲢𞲣𞲤	𞲥	𞲦	𞲧 
#     ä, ö, ü, Ä, Ö, Ü µ ﬁ ﬄ
#     """
# print(a.casefold())

# s1 = "hi hello world meow meow meow"
# print(s1.find("hello"))
# print(s1.find("hellow"))
# print(s1.find("WORLD"))

s1 = " hello"
print(s1.startswith("hello"))
print(s1.startswith(" "))
print(s1.startswith(""))
print("------------")
s1 = " hello "
print(s1.endswith("hello"))
print(s1.endswith(" "))
print(s1.endswith(""))
print("------------")
text = "I like Java"
new_text = text.replace("Java", "Python")
print(new_text)
print(text)