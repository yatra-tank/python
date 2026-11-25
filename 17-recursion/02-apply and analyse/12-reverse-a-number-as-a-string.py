# Write reverse_text(text) that returns the characters of a string in reverse order using recursion.
def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]