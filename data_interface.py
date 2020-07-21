from data_structure import *

def getSentence(index):
    return all_data[index]

def getSentIndex(word):
    return data_structure[word]

def sort_sentences(word_list):
    sorted = [all_data[word] for word in word_list].sort()
    return [all_data.index(word) for word in word_list]

def offset(index, word):
    return all_data[index].find(word)
