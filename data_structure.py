from collections import defaultdict
from auxiliary_functions import *

file_data = []
all_data = []
data_structure = defaultdict(set)
file_source = {0: "about.txt", 1: "temp.txt"}
data_source = {}
data_offset = {}


def sort_data(word_list):
    word_list = [all_data[word] for word in word_list]
    word_list.sort()
    return [all_data.index(word) for word in word_list]

def files_reader():
    for key, value in file_source.items():
        with open(value) as the_file:
            global file_data
            file_data += the_file.read().split("\n")
        for i, sent in enumerate(file_data):
            data_source[len(all_data)] = key
            data_offset[len(all_data)] = i
            all_data.append(sent)

def data_initialization():
    files_reader()

    for i in range(len(all_data)):
        for j in range(len(all_data[i])):
            for k in range(j + 1, len(all_data[i]) + 1):
                global data_structure
                data_structure[ignore_delimiters(all_data[i][j:k])].add(i)
                data_structure[ignore_delimiters(all_data[i][k:j])].add(i)

    data_structure.pop('')

    for sen in data_structure.keys():
        if len(data_structure[sen]) > 5:
            data_structure[sen] = set(sort_data(data_structure[sen])[:5])


data_initialization()

