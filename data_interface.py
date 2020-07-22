from auto_complete_data import AutoCompleteData
from data_structure import *


def get_sentence(index):
    return all_data[index]


def get_sentIndex(word):
    return data_structure[word]


def get_sentence_src(index):
    return data_source[index]


def offset(index, word):
    return all_data[index].find(word)
    pass


def sentences_after_fixing(word, best_completions):
    equal = -1
    results = []
    for i in range(len(word)-1,-1,-1):
        if(-1 == equal):
            for ltr in range(ord('a'), ord('z')):
                index = data_structure.get(word[:i] + "ltr" + word[i+1:])
                if index:
                    equal = i
                    results = [word for word in index]
                    break

    new_word = word[:equal]+ ltr + word[equal+1:]
    if equal > 0:
        results = sort_sentences(results)

    score = 5-equal if equal<5 else 1

    on_top = 5-len(best_completions)
    num_of_elements = on_top if len(results) > on_top else len(results)
    for i in range(num_of_elements):
        best_completions.append(AutoCompleteData(get_sentence(results[i]), "", offset(results[i], new_word), len(word) * 2 - score))

    return best_completions


