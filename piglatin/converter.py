"""Pig Latin Text Conterter."""

from string import punctuation, ascii_letters

def is_punctuation(word):
    return len(set(punctuation) & set(word))

def is_letters_only(word):
    return len(set(ascii_letters) & set(word))

def punctiation_handl(word):
    special_chars = set(punctuation)
    if word[-1] not in special_chars:
        return plain_word_handl(word)

    for i in special_chars:
        idx = word.find(i)
        if idx != -1:
            return plain_word_handl(word[:idx]) + word[idx:]
#lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']

def plain_word_handl(word):
    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxyz"+"bcdfghjklmnpqrstvwxyz".upper())
    new_word = list(word)
    if word[0] in vowels:
        return word + "yay"

    for letter in word:
        if letter in consonants:
            temp = new_word.pop(0)
            new_word.append(temp)
        else:
            break
    return "".join(new_word) + "ay"

def convert_text(text):
    new_text = []
    for word in text.split(" "):
        new_text.append(convert_word(word))
    return " ".join(new_text)

def convert_word(word):
    if not is_letters_only(word): #if word contained no ascii_letters (only numbers and punctuation)
        return word

    title = False
    if word.istitle():
        word = word.lower()
        title = True

    if is_punctuation(word):
        if title:
            return punctiation_handl(word).capitalize()
        else:
            return punctiation_handl(word)
    else:
        if title:
            return plain_word_handl(word).capitalize()
        else:
            return plain_word_handl(word)


def test(switch):
    w = ["pig", "banana", "trash", "happy", "duck", "glove", "eat", "omlet", "are"]
    text = '''Hello, my name is haha - is haha, Is 2017 Awesome Gram M&N I am Charlie's beast mama my friend!'''

    if switch == "word":
        for i in w:
            print i, " => ", convert_word(i)
    elif  switch == "text":
        print text
        print convert_text(text)

def main():
    pass

if __name__ == '__main__':
    main()
