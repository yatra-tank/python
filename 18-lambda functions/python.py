words = ["apple", "kiwi", "banana", "fig"]

result = sorted(
    words,
    key=lambda word: len(word),
)

print(result)