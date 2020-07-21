from data_structure import *

def getSentence(index):
    return all_data[index]

def getSentIndex(word):
    return data_structure[word]

def sort_sentences(word_list):
    return [all_data[word] for word in word_list].sort()