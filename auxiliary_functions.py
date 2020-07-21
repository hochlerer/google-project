import re


def ignore_delimiters(word):
    word = word.lower()
    return "".join(re.split("[\W+ _]", word))
