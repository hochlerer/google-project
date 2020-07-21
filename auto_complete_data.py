class AutoCompleteData:
    def __init__(self, sent, src, ofst, rating):
        self.__completed_sentence = sent
        self.__source_text = src
        self.__offset = ofst
        self. __score = rating

    def get_sentence(self):
        return self.__completed_sentence

    def get_source_text(self):
        return self.__source_text

    def get_offset(self):
        return self.__offset

    def get_score(self):
        return self.__score

