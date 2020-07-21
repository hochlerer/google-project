from data_interface import *
# hide data

def complete(prefix):
    results = [word for word in getSentIndex(prefix)]

    for i in results:
        print(getSentence(i))

        # return auto data