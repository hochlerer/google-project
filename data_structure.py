from collections import defaultdict
from auxiliary_functions import *

all_data = []
data_structure = defaultdict(set)

def data_initialization():
    with open("about.txt") as data_file:
        global all_data
        all_data = data_file.read().split("\n")

    for i in range(len(all_data)):
        for j in range(len(all_data[i])):
            for k in range(j + 1, len(all_data[i]) + 1):
                data_structure[ignore_delimiters(all_data[i][j:k])].add(i)
                data_structure[ignore_delimiters(all_data[i][k:j])].add(i)

    data_structure.pop("")



