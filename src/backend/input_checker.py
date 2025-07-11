from .db_handler import DBHandler
class InputChecker:
    def __init__(self):
        self.db = DBHandler("demo.db")
        self.lections = 2 # TODO: adapt to frontend interface.
        self.founded = []
        self.unfounded = []
        self.answer = []

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

    def get_input(self, input):
        #sentence = "Puellae servae sunt. Equus bonus est!" # TODO: adapt to frontend interface.
        sentence = input.lower()
        sentence = self._remove_punctuation_marks(sentence)
        words = sentence.split()
        return words
    
    def _check(self, words: list[str]):
        for word in words:
            temp = word
            while len(temp) > 0:
                for lection in range (self.lections):
                    lection += 1 #adapted to lection names
                    exists, result = self.db.check_if_exists(temp, lection)
                    if exists:
                        self.founded.append(f"{word} (Infinitive: {result[1]}, Tribe: {result[2]}, German: {result[3]}) was founded in Lection {lection}")
                        self.answer.append({"vocab": result[1], "in_db":exists})
                        break
                if exists:
                    break
                temp = temp[:-1]
            if not exists:
                self.unfounded.append(word)
                self.answer.append({"vocab": word, "in_db":exists})
            #self.answer.append({"vocab": result[1], "in_db":exists})
        return self.answer

    def main(self, input: str):
        words = self.get_input(input)
        answer = self._check(words)
        return answer

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