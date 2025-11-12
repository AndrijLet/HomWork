def remove_chars(word, n):
    """
    перевірка що n менше довжини рядка
    checking that n is less than the length of the string
    """
    if n < len(word):
        return word[:n]
    else:
        return "Eror: n is greater that string length"

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))