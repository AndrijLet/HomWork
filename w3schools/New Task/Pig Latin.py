VOWELS = 'aeiouy'
word = input("Введіть слово: ").lower()

if word in VOWELS:
    pig_latin = word + "way"

else:
    # word[1:] - беремо все після першої літери, word - перша літера
    pig_latin = word[1:] + word + "ay"

print(f"Результат: {pig_latin}")