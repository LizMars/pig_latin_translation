"""Pig Latin Text Converter."""

from string import punctuation, ascii_letters, whitespace
import re

def is_punctuation(word):
    return len(set(punctuation) & set(word))

def is_letters_only(word):
    return len(set(ascii_letters) & set(word))

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
    regexp = r"[\w']+|[{punc}{space}]".format(punc=punctuation, space=whitespace)
    tokens = re.findall(regexp, text)
    new_text = [convert_word(token) for token in tokens]
    print "".join(new_text)
    return "".join(new_text)

def convert_word(word):
    if is_letters_only(word): #if word contained no ascii_letters (only numbers and punctuation)
        title = False
        if word.istitle():
            word = word.lower()
            title = True
        if title:
            return plain_word_handl(word).capitalize()
        else:
            return plain_word_handl(word)
    else:
        return word


def main():
    pass

if __name__ == '__main__':
    main()
