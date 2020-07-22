from complete import *
from data_structure import data_initialization

def start_App():
    data_initialization()
    while(1):
        print("Enter your text: ")
        input_ = input()
        while input_ != "#":
            print("Here are 5 suggestions")
            complete(input_)
            print(input_, end=" ")
            input_ = input_ +" " + input()


start_App()