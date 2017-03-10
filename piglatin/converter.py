"""Pig Latin Text Conterter."""
from string import punctuation

def is_punctuation(word):
    return len(set(punctuation) & set(word))

def punctiation_handl(word):
    special_chars = set(punctuation)
    for i in special_chars:
        idx = word.find(i)
        if idx != -1:
            return plain_word_handl(word[:idx]) + word[idx:]

def plain_word_handl(word):
    consonants = set("bcdfghjklmnpqrstvwxyz")
    new_word = list(word)
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
    title = False
    if word.istitle():
        word.lower()
        title = True

    if not word.isalpha():
        return word

    elif is_punctuation(word):
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
    text = '''Listen on port, 80 and accept a string that contains at least
    one word, but potentially entire paragraphs. Convert the words in the
    string: to Pig Latin and return the results in the HTTP message body!?
    * Preserve all of the punctuation in the original string.'''

    if switch == "word":
        for i in w:
            print i, " => ", convert_word(i)
    elif  switch == "text":
        print text
        print convert_text(text)



def main():
    #word, text
    test("text")

if __name__ == '__main__':
    main()
