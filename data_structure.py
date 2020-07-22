from collections import defaultdict
from auxiliary_functions import *

all_data = []
data_structure = defaultdict(set)
data_source = {}

def sort_data(word_list):
    word_list = [all_data[word] for word in word_list]
    word_list.sort()
    return [all_data.index(word) for word in word_list]

def data_initialization():
    with open("about.txt") as data_file:
        global all_data
        all_data = data_file.read().split("\n")

    for i in range(len(all_data)):
        for j in range(len(all_data[i])):
            for k in range(j + 1, len(all_data[i]) + 1):
                global data_structure
                data_structure[ignore_delimiters(all_data[i][j:k])].add(i)
                data_structure[ignore_delimiters(all_data[i][k:j])].add(i)

    for i in range(len(all_data)):
        data_source[i] = "about.txt"

    data_structure.pop("")

    for sen in data_structure.keys():
        if len(data_structure[sen]) > 5:
            data_structure[sen] = set(sort_data(data_structure[sen])[:5])


data_initialization()

