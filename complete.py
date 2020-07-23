from data_interface import *
from auxiliary_functions import *
from auto_complete_data import AutoCompleteData


def replace_char(word, best_indexes):
    on_top = 5 - len(best_indexes)
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
                    if j not in best_indexes:
                        results.append({"sentence_index": j,
                                        "src": j,
                                        "offset": offset(j),
                                        "score": len(word) * 2 - score})
                        best_indexes.append(j)
                break

    return results[:on_top]


def delete_char(word, best_indexes):
    on_top = 5- len(best_indexes)
    results = []
    for i in range(len(word) - 1, -1, -1):
        if len(results) != 0:
            break
        for ltr in range(ord('a'), ord('z') + 1):
            new_word = word[:i] + chr(ltr) + word[i:]
            indexes = data_structure.get(new_word)
            if indexes:
                score = 10 - 2 * i if i < 4 else 2
                for j in indexes:
                    if j not in best_indexes:
                        results.append({"sentence_index": j,
                                        "src": j,
                                        "offset": offset(j),
                                        "score": len(word) * 2 - score})
                        best_indexes.append(j)
                break

    return results[:on_top]


def add_char(word, best_indexes):
    on_top = 5- len(best_indexes)
    results = []
    for i in range(len(word)-1, -1, -1):
        new_word = word[:i] + word[i+1:]
        indexes = data_structure.get(new_word)
        if indexes:
            score = 10 - 2*i if i < 4 else 2
            for j in indexes:
                if j not in best_indexes:
                    results.append({"sentence_index": j,
                                    "src": j,
                                    "offset": offset(j),
                                    "score": len(word) * 2 - score})
                    best_indexes.append(j)
            break

    return results[:on_top]


def fix_word(word, best_sentences):
    on_top = 5- len(best_sentences)
    best_indexes = best_sentences[::]
    replace = replace_char(word, best_indexes)
    delete = delete_char(word, best_indexes)
    add = add_char(word, best_indexes)

    most_rate = replace + delete + add
    most_rate = sorted(most_rate, key=lambda k: k["score"], reverse=True)
    return most_rate[:on_top]


def complete(prefix):
    prefix_ignore_del = ignore_delimiters(prefix)
    results = [word for word in get_sentIndex(prefix_ignore_del)]
    best_completions = []

    for i in range(len(results)):
        best_completions.append(AutoCompleteData(get_sentence(results[i]), get_sentence_src(results[i]), offset(results[i]), len(prefix) * 2))

    fit_sents = fix_word(prefix_ignore_del, results)
    for sent in fit_sents:
        best_completions.append(AutoCompleteData(get_sentence(sent["sentence_index"]), get_sentence_src(sent["src"]), sent["offset"], sent["score"]))

    return best_completions
