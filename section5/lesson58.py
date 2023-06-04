l = ["Mon", "tue", "Wed", "Thu", "fri", "sat", "Sun"]


def change_words(words, func):
    for word in words:
        print(func(word))


def capitalize(word):
    return word.capitalize()


lambda_capitalize = lambda word: word.capitalize()

change_words(l, capitalize)
change_words(l, lambda_capitalize)
change_words(l, lambda word: word.capitalize())

change_words(l, lambda word: word.lower())
