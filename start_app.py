from data_structure import data_initialization
from complete import *



def start_App():
    while(1):
        print("Enter your text: ")
        input_ = input()
        while input_[-1] != "#":
            print("Here are 5 suggestions")
            suggestions = complete(input_)
            for sent in suggestions:
                print(sent.get_sentence())
            print(input_, end="")
            input_ = input_ + input()


start_App()