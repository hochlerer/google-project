from data_interface import *
from auxiliary_functions import *
from auto_complete_data import AutoCompleteData
# hide data

def complete(prefix):
    prefix_ignore_del = ignore_delimiters(prefix)
    results = [word for word in get_sentIndex(prefix_ignore_del)]
    best_completions = []

    num_of_elements = len(results) if len(results) < 5 else 5

    for i in range(num_of_elements):
        # offset- עם תוים?
        best_completions.append(AutoCompleteData(get_sentence(results[i]), get_sentence_src(results[i]), offset(results[i], prefix), len(prefix) * 2))

    fit_sents = fix_word(prefix_ignore_del, 5- len(best_completions))
    for sent in fit_sents:
        best_completions.append(AutoCompleteData(get_sentence(sent["sentence_index"]), get_sentence_src(sent["src"]), sent["offset"], sent["score"]))

    return best_completions
    # if(len(results)<5):
    #     temp1 = sentences_after_fixing(prefix_ignore_del, best_completions[::])
    # # החלפה
    #     pass
    #
    # if(len(results)<5):
    #     temp2 = sentences_after_change(prefix_ignore_del, best_completions[::])
    # # מחיקה
    #     pass

    # what should i prefer? temp1 / temp2?

    return best_completions