from auto_complete_data import AutoCompleteData
from data_structure import *


def get_sentence(index):
    return all_data[index]


def get_sentIndex(word):
    return data_structure[word]


def get_sentence_src(index):
    return data_source[index]


def offset(index, word):
    return get_sentence(index).find(word)

def replace_char(word, on_top):
    results = []
    for i in range(len(word)-1, -1, -1):
        if len(results) != 0:
            break
        for ltr in range(ord('a'), ord('z')+1):
            new_word = word[:i] + chr(ltr) + word[i+1:]
            indexes = data_structure.get(new_word)
            if indexes:
                score = 5 - i if i < 5 else 1
                for j in indexes:
                    results.append({"sentence_index": j,
                                    "src": j,
                                    "offset": offset(j, new_word),
                                    "score": len(word) * 2 - score})
                break

    return results[:on_top]


def delete_char(word, on_top):
    pass


def add_char(word, on_top):
    pass


def fix_word(word, on_top):
    replace = replace_char(word, on_top)
    delete = delete_char(word, on_top)
    add = add_char(word, on_top)

    # if len(replace) == on_top:
    #     if len(delete) == on_top:
    #         if len(add) == on_top:
    #             return
    return replace


