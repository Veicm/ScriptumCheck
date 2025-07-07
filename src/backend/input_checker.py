class InputChecker:
    def __init__(self):
        self.voc = ["puell", "serv", "est", "equ", "bon"] # TODO: replace with database integration.
        self.founded = []
        self.unfounded = []

    def _remove_punctuation_marks(self, input:str) ->str:
        temp = input.replace(".", "")
        temp = temp.replace(",", "")
        temp = temp.replace(":", "")
        temp = temp.replace(";", "")
        temp = temp.replace("!", "")
        temp = temp.replace("?", "")
        temp = temp.replace('"', '')
        temp = temp.replace("(", "")
        result = temp.replace(")", "")
        return result

    def get_input(self):
        sentence = "Puellae servae sunt. Equus bonus est!" # TODO: adapt to frontend interface.
        sentence = sentence.lower()
        sentence = self._remove_punctuation_marks(sentence)
        words = sentence.split()
        return words
    
    def _check(self, words):
        for word in words:
            temp = word
            while len(temp) > 0:
                if temp in self.voc:
                    self.founded.append(f"{word} (tribe: {temp})")
                    exists = True
                    break
                else:
                    temp = temp[:-1]
                    exists = False
            if not exists:
                self.unfounded.append(word)
    
    def output(self): # TODO: adapt to frontend interface.
        input = self.get_input()
        self._check(input)
        print("The following words could not be found in the vocabulary:")
        for word in self.unfounded:
            print(word)
        print("PLease try to search the infinitive.")
        print("")
        print("The following word could be found in the vocabulary:")
        for word in self.founded:
            print(word)

def main():
    ic = InputChecker()
    ic.output()

if __name__ == "__main__":
    main()