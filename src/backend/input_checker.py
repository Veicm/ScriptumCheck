from .db_handler import DBHandler

class InputChecker:
    """
    Contains needed functions to check if the word in a sentence are in the DB.

    Attributes:
        None
    """
    def __init__(self) -> None:
        self.db = DBHandler("demo.db")# TODO: change to actual database.

    def _remove_punctuation_marks(self, input: str) -> str:
        """
        Removes punctuation marks from a given sentence.

        Args:
            input (str): The sentence from which the punctuation marks should be removed.

        Returns:
            str: The sentence without punctuation marks.
        """
        temp = input.replace(".", "")
        temp = temp.replace(",", "")
        temp = temp.replace(":", "")
        temp = temp.replace(";", "")
        temp = temp.replace("!", "")
        temp = temp.replace("?", "")
        temp = temp.replace('"', '')
        temp = temp.replace("'", "")
        temp = temp.replace("(", "")
        result = temp.replace(")", "")
        return result

    def _get_input(self, input: str) -> list[str]:
        """
        Converts a given text into a list of lowercase words.

        Args:
            input (str): The sentence which should be converted.

        Returns:
            List[str]: A list of the lowercased words from the sentence.
        """
        sentence: str = input.lower()
        sentence: str = self._remove_punctuation_marks(sentence)
        words: list[str] = sentence.split()
        return words
    
    def _check(self, words: list[str], lections: int = 2, extended: bool = False) -> list[dict[str, bool]]: #TODO: remove default value for lections when integrated.
        """
        Checks whether the given words exist in the database across the specified number of lections.

        The function attempts to match each word (or its truncated stems) against vocabulary entries
        in the database for each lection. If a match is found, the result is stored along with 
        metadata (infinitive, tribe, translation). If no match is found, the word is recorded as unfounded.

        Args:
            words (list[str]): A list of words to be checked.
            lections (int): The number of lections (lessons) to search through.
            extended (bool, optional): If True, returns detailed match information. Defaults to False.

        Returns:
            list[dict[str, bool]]: A list of dictionaries with keys:
                - "vocab": the infinitive form of the found word or the original if not found.
                - "in_db": True if the word was found, False otherwise.

            If `extended` is True, the return value is a tuple, its recommended to save in three different variables:
                (
                    answer (list[dict[str, bool]]),
                    founded (list[str]): Human-readable strings for found words,
                    unfounded (list[str]): Words that could not be matched in any lection
                )
        """
        founded: list[str] = []
        unfounded: list[str] = []
        answer: list[dict[str, bool]] = []
        for word in words:
            temp = word
            while len(temp) > 0:
                for lection in range (lections):
                    lection += 1 # adapted to lection names
                    exists, result = self.db.check_if_exists(temp, lection)
                    if exists:
                        founded.append(f"{word} (Infinitive: {result[1]}, Tribe: {result[2]}, German: {result[3]}) was founded in Lection {lection}")
                        answer.append({"vocab": result[1], "in_db":exists})
                        break
                if exists:
                    break
                temp = temp[:-1]
            if not exists:
                unfounded.append(word)
                answer.append({"vocab": word, "in_db":exists})
        if not extended:
            return answer
        elif extended:
            return answer, founded, unfounded

    def main(self, input: str, lections: int = 2) -> list[dict[str, bool]]:# TODO: Remove default value for lection when integrated.
        """
        The main function of the class which is used to check if the words in a text can be found in the DB.

        The function first separates the text into word and scans them afterwards.

        Args:
            input (str): The text which should be scanned.
            lections (int): The number of lections (lessons) to search through.

        Returns:
            list[dict[str, bool]]: A list of dictionaries with keys:
                - "vocab": the infinitive form of the found word or the original if not found.
                - "in_db": True if the word was found, False otherwise.
        """
        words: list[str] = self._get_input(input)
        answer: list[dict[str, bool]] = self._check(words, lections)
        return answer
    
    def output(self) -> None:
        """
        Outputs the result of the _check() function with a give demo text.
    
        Args:
            None
    
        Returns:
            None
        """
        words: list[str] = self._get_input("Puellae servae sunt. Equus bonus est!")# Demo Text
        answer, founded, unfounded = self._check(words, 2, True)
        print("The following words could be founded:")
        print(founded)
        print("")
        print("The following words could not be founded in the given lections:")
        print(unfounded)
        print("")
        print("This is the program intern result:")
        print(answer)

def main() -> None:
    ic = InputChecker()
    ic.output()

if __name__ == "__main__":
    main()